// Reveals .reveal elements once they scroll into view.
(function () {
  var reveal = function (el) {
    el.classList.add('revealed');
  };

  var reduced = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var items = document.querySelectorAll('.reveal');

  // No observer or reduced motion: show everything at once.
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach(reveal);
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      reveal(entry.target);
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  items.forEach(function (el) {
    observer.observe(el);
  });
})();
