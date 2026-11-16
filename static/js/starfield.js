// Occasional shooting stars for <canvas data-starfield>.
// The canvas must live inside a positioned element (a <section>) that has a
// background image; streaks are kept over the dark parts of that image.
(function () {
  var canvases = document.querySelectorAll('canvas[data-starfield]');
  if (!canvases.length) return;

  var mq = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : null;
  if (mq && mq.matches) return; // decoration only: draw nothing

  var DPR = Math.min(window.devicePixelRatio || 1, 2);
  // Luminance (0-1) where streaks are allowed / must disappear. Measured on the
  // hero photo: open space ~0.01-0.07, shadowed ocean ~0.19, lit globe ~0.33.
  var LOW = 0.05, HIGH = 0.18;
  var masks = {}; // image URL -> {w, h, lum, iw, ih} | null while loading | false

  // Sample an image into a luminance map, once per URL. The map is downscaled
  // for sampling; iw/ih keep the real pixel size, which background-size: auto
  // needs. Returns null while loading, false if it cannot be read.
  function maskFor(url) {
    if (masks[url] === undefined) {
      masks[url] = null;
      var img = new Image();
      img.onload = function () {
        var w = Math.min(img.width, 240);
        var h = Math.max(1, Math.round(w * img.height / img.width));
        var off = document.createElement('canvas');
        off.width = w;
        off.height = h;
        var octx = off.getContext('2d');
        octx.drawImage(img, 0, 0, w, h);
        try {
          var d = octx.getImageData(0, 0, w, h).data;
          var lum = new Float32Array(w * h);
          for (var i = 0, p = 0; i < lum.length; i++, p += 4) {
            lum[i] = (0.2126 * d[p] + 0.7152 * d[p + 1] + 0.0722 * d[p + 2]) / 255;
          }
          masks[url] = { w: w, h: h, lum: lum, iw: img.width, ih: img.height };
        } catch (e) {
          masks[url] = false; // tainted canvas or decode failure: no mask
        }
      };
      img.onerror = function () { masks[url] = false; };
      img.src = url;
    }
    return masks[url];
  }

  // --- background geometry ---------------------------------------------------
  // A section can stack several layers (the home hero puts a jxl over an avif),
  // and each layer carries its own attachment/position/size. Computed values
  // are parallel comma lists, so split them before reading anything: comparing
  // backgroundAttachment against 'fixed' fails when it comes back as "fixed, fixed".

  function splitTop(s) {
    var out = [], cur = '', depth = 0, q = '';
    for (var i = 0; i < s.length; i++) {
      var c = s.charAt(i);
      if (q) { cur += c; if (c === q) q = ''; continue; }
      if (c === '"' || c === "'") { q = c; cur += c; continue; }
      if (c === '(') depth++;
      else if (c === ')') depth--;
      else if (c === ',' && !depth) { out.push(cur.trim()); cur = ''; continue; }
      cur += c;
    }
    if (cur.trim()) out.push(cur.trim());
    return out;
  }

  function at(list, i, dflt) { return list[i] === undefined ? dflt : list[i]; }

  // Layers in paint order (first = topmost), each with its raw geometry rules.
  function backgroundLayers(cs) {
    var imgs = splitTop(cs.backgroundImage || 'none');
    if (imgs.length === 1 && imgs[0] === 'none') return [];
    var att = splitTop(cs.backgroundAttachment || 'scroll');
    var pos = splitTop(cs.backgroundPosition || '0% 0%');
    var size = splitTop(cs.backgroundSize || 'auto');
    var layers = [];
    for (var i = 0; i < imgs.length; i++) {
      var m = /url\((['"]?)(.*?)\1\)/.exec(imgs[i]);
      if (!m) continue;
      layers.push({
        url: m[2],
        attachment: at(att, i, 'scroll'),
        position: axisPair(at(pos, i, '0% 0%')),
        size: at(size, i, 'auto')
      });
    }
    return layers;
  }

  // "50% 0%" / "center top" -> [{pct,v},{pct,v}]; v is px when pct is false.
  function axisPair(spec) {
    var t = String(spec).trim().split(/\s+/);
    return [axis(t[0]), axis(t[1] === undefined ? '50%' : t[1])];
  }

  function axis(tok) {
    if (!tok || tok === 'center') return { pct: true, v: 0.5 };
    if (tok === 'left' || tok === 'top') return { pct: true, v: 0 };
    if (tok === 'right' || tok === 'bottom') return { pct: true, v: 1 };
    var n = parseFloat(tok);
    if (isNaN(n)) return { pct: true, v: 0.5 };
    return tok.charAt(tok.length - 1) === '%' ? { pct: true, v: n / 100 } : { pct: false, v: n };
  }

  // Painted size of one layer, in px (background-size: cover/contain/auto/len).
  function paintedSize(spec, box, iw, ih) {
    var t = String(spec).trim().split(/\s+/);
    if (t[0] === 'cover' || t[0] === 'contain') {
      var k = t[0] === 'cover'
        ? Math.max(box.w / iw, box.h / ih)
        : Math.min(box.w / iw, box.h / ih);
      return { w: iw * k, h: ih * k };
    }
    return { w: length(t[0], box.w, iw), h: length(t[1], box.h, ih) };
  }

  function length(tok, base, auto) {
    if (!tok || tok === 'auto') return auto;
    var n = parseFloat(tok);
    if (isNaN(n)) return auto;
    return tok.charAt(tok.length - 1) === '%' ? base * n / 100 : n;
  }

  function Stars(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.section = canvas.parentElement;
    this.star = null;
    this.raf = 0;
    this.timer = 0;
    this.running = false;
    this.onScreen = false;
    this.rect = { left: 0, top: 0 };
    this.layer = null; // layer that is actually painted
    this.mask = null;  // luminance map of that layer
    this.geo = null;   // where that layer sits, in viewport terms
    this.measure();
  }

  // Canvas backing size, then re-read the background.
  Stars.prototype.measure = function () {
    var rect = this.canvas.getBoundingClientRect();
    this.w = Math.round(rect.width);
    this.h = Math.round(rect.height);
    if (!this.w || !this.h) return;
    this.canvas.width = Math.round(this.w * DPR);
    this.canvas.height = Math.round(this.h * DPR);
    this.ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    this.resolve();
    if (this.layer) this.build();
  };

  // The painted layer is the first whose image decodes: lower layers are
  // fallbacks (a browser without jxl support paints the avif underneath).
  Stars.prototype.resolve = function () {
    var layers = backgroundLayers(window.getComputedStyle(this.section));
    for (var i = 0; i < layers.length; i++) {
      var m = maskFor(layers[i].url);
      if (m === null) return;     // still decoding the top layer
      if (m === false) continue;  // unusable, try the next one
      if (this.mask !== m) {
        this.layer = layers[i];
        this.mask = m;
        this.build();
      }
      return;
    }
    this.layer = this.mask = this.geo = null;
  };

  // Where the painted layer sits: fixed layers use the viewport as their box,
  // scrolling ones use the section, and background-size decides the rest.
  Stars.prototype.build = function () {
    var y = this.layer, m = this.mask;
    if (!y || !m) { this.geo = null; return; }
    var fixed = y.attachment === 'fixed';
    var box = fixed
      ? { w: window.innerWidth, h: window.innerHeight }
      : { w: this.w, h: this.h };
    var s = paintedSize(y.size, box, m.iw, m.ih);
    this.geo = {
      fixed: fixed,
      w: s.w,
      h: s.h,
      x: y.position[0].pct ? (box.w - s.w) * y.position[0].v : y.position[0].v,
      y: y.position[1].pct ? (box.h - s.h) * y.position[1].v : y.position[1].v
    };
  };

  // Live position of the canvas, needed to map viewport points to the photo.
  Stars.prototype.sync = function () {
    var rect = this.canvas.getBoundingClientRect();
    this.rect.left = rect.left;
    this.rect.top = rect.top;
  };

  // How star-friendly the photo is at a viewport point: 1 = open sky, 0 = bright.
  Stars.prototype.sky = function (vx, vy) {
    var m = this.mask, g = this.geo;
    // No mask yet, or none could be read: draw nothing. Without it we cannot
    // tell sky from lit surface, and streaks over a planet look wrong.
    if (!m || !g) return 0;

    // Into the background image's own box.
    var u = ((g.fixed ? vx : vx - this.rect.left) - g.x) / g.w;
    var v = ((g.fixed ? vy : vy - this.rect.top) - g.y) / g.h;
    // Uncovered area shows the section's backdrop, which is dark: open sky.
    if (u < 0 || u > 1 || v < 0 || v > 1) return 1;

    // Brightest luminance in a small neighbourhood: keeps streaks a few pixels
    // clear of dark/bright edges, where a single cell can fall on the bright side.
    var cx = u * m.w | 0, cy = v * m.h | 0, l = 0;
    for (var j = -1; j <= 1; j++) {
      for (var i = -1; i <= 1; i++) {
        var xx = cx + i < 0 ? 0 : cx + i >= m.w ? m.w - 1 : cx + i;
        var yy = cy + j < 0 ? 0 : cy + j >= m.h ? m.h - 1 : cy + j;
        l = Math.max(l, m.lum[yy * m.w + xx]);
      }
    }
    if (l <= LOW) return 1;
    if (l >= HIGH) return 0;
    return 1 - (l - LOW) / (HIGH - LOW);
  };

  // Wait a few seconds, then try to start a streak; retry sooner while the
  // photo mask is still loading, later if nothing dark enough was found.
  Stars.prototype.schedule = function (delay) {
    var self = this;
    clearTimeout(this.timer);
    this.timer = setTimeout(function () {
      self.resolve(); // pick up the mask once it finishes decoding
      if (!(self.running && self.start())) {
        self.schedule(self.mask ? 2500 + Math.random() * 5000 : 800);
      }
    }, delay === undefined ? 2500 + Math.random() * 5000 : delay);
  };

  Stars.prototype.start = function () {
    this.sync();
    for (var tries = 0; tries < 8; tries++) {
      var fromRight = Math.random() < 0.6;
      var x = fromRight ? this.w * (0.55 + Math.random() * 0.4) : Math.random() * this.w * 0.4;
      var y = Math.random() * this.h * 0.5;
      if (this.sky(this.rect.left + x, this.rect.top + y) > 0.6) {
        this.star = {
          x: x, y: y, last: 0, life: 1,
          vx: fromRight ? -(4 + Math.random() * 3) : 4 + Math.random() * 3,
          vy: 1.6 + Math.random() * 1.6
        };
        this.raf = window.requestAnimationFrame(this.step.bind(this));
        return true;
      }
    }
    return false;
  };

  Stars.prototype.step = function (now) {
    var s = this.star;
    if (!s) return;
    var k = s.last ? Math.min(now - s.last, 50) / 16.7 : 1; // frame-rate independent
    s.last = now;
    this.sync();

    s.x += s.vx * k * 3;
    s.y += s.vy * k * 3;
    s.life -= 0.012 * k;

    var head = this.sky(this.rect.left + s.x, this.rect.top + s.y);
    this.ctx.clearRect(0, 0, this.w, this.h);

    // Ends on the bright part of the photo instead of drawing over it.
    if (s.life <= 0 || head < 0.25 || s.x < -40 || s.x > this.w + 40) {
      this.star = null;
      this.raf = 0;
      this.schedule();
      return;
    }

    // Tail as short segments, each faded by how dark the photo is under it.
    var tailX = s.x - s.vx * 10;
    var tailY = s.y - s.vy * 10;
    var N = 8;
    this.ctx.globalCompositeOperation = 'lighter';
    this.ctx.lineWidth = 1.5;
    this.ctx.lineCap = 'round';
    for (var i = 0; i < N; i++) {
      var a = i / N, b = (i + 1) / N;
      var x0 = s.x + (tailX - s.x) * a, y0 = s.y + (tailY - s.y) * a;
      var x1 = s.x + (tailX - s.x) * b, y1 = s.y + (tailY - s.y) * b;
      var vis = this.sky(this.rect.left + (x0 + x1) / 2, this.rect.top + (y0 + y1) / 2);
      var alpha = Math.max(s.life, 0) * (1 - a) * vis;
      if (alpha < 0.03) continue;
      this.ctx.strokeStyle = 'rgba(255,255,255,' + alpha.toFixed(2) + ')';
      this.ctx.beginPath();
      this.ctx.moveTo(x0, y0);
      this.ctx.lineTo(x1, y1);
      this.ctx.stroke();
    }
    this.ctx.globalCompositeOperation = 'source-over';

    this.raf = window.requestAnimationFrame(this.step.bind(this));
  };

  Stars.prototype.play = function () {
    if (this.running) return;
    this.running = true;
    this.measure();
    this.schedule();
  };

  Stars.prototype.pause = function () {
    this.running = false;
    clearTimeout(this.timer);
    if (this.raf) window.cancelAnimationFrame(this.raf);
    this.raf = 0;
    this.star = null;
    if (this.w) this.ctx.clearRect(0, 0, this.w, this.h);
  };

  var stars = [];
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      entry.target._stars.onScreen = entry.isIntersecting;
    });
    refresh();
  }, { threshold: 0 }) : null;

  // Animate only on screen and on a visible tab.
  function refresh() {
    stars.forEach(function (st) {
      if (st.onScreen && !document.hidden) st.play(); else st.pause();
    });
  }

  Array.prototype.forEach.call(canvases, function (canvas) {
    if (!canvas.getContext || !canvas.parentElement) return;
    var st = new Stars(canvas);
    canvas._stars = st;
    stars.push(st);
    if (io) io.observe(canvas); else st.onScreen = true;
  });

  document.addEventListener('visibilitychange', refresh);

  if ('ResizeObserver' in window) {
    var ro = new ResizeObserver(function () { stars.forEach(function (st) { st.measure(); }); });
    stars.forEach(function (st) { ro.observe(st.canvas); });
  } else {
    window.addEventListener('resize', function () { stars.forEach(function (st) { st.measure(); }); });
  }

  refresh();
})();
