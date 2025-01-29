$(randompic)

function randompic() {
    var bgm = ['/img/screenshots/aurora.jpg','/img/screenshots/trifid.jpg', '/img/screenshots/asteroids.jpg', '/img/screenshots/bh.jpg', '/img/screenshots/constel.jpg', '/img/screenshots/crab.jpg', '/img/screenshots/datasets.jpg', '/img/screenshots/earthrise.jpg', '/img/screenshots/enterprise.jpg', '/img/screenshots/exoplanets.jpg', '/img/screenshots/exoplanets02.jpg', '/img/screenshots/exoplanets03.jpg', '/img/screenshots/gaia.jpg', '/img/screenshots/hst.jpg', '/img/screenshots/iss.jpg', '/img/screenshots/iss2.jpg', '/img/screenshots/moon.jpg', '/img/screenshots/saturn.jpg', '/img/screenshots/scattering.jpg', '/img/screenshots/sdss.jpg', '/img/screenshots/voyager.jpg'];
 
    $('.random-background').css({
        'background-image' : 'url('+ bgm[Math.floor(Math.random() * bgm.length)] + ')',
    });
}
