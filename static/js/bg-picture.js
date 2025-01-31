$(randompic)

function randompic() {
    var bgm = [
        'asteroids.jpg',
        'aurora.jpg',
        'blackhole.jpg',
        'constel.jpg',
        'crab.jpg',
        'datasets.jpg',
        'earthrise.jpg',
        'enterprise.jpg',
        'exoplanets.jpg',
        'gaia.jpg',
        'hst.jpg',
        'hst2.jpg',
        'iss.jpg',
        'iss2.jpg',
        'moon.jpg',
        'saturn.jpg',
        'scattering.jpg',
        'sdss.jpg',
        'trifid.jpg',
        'voyager.jpg'];
 
    var path = window.location.pathname;
    $('.random-background').css({
        'background-image' : 'url(/gaiasky/web/img/backgrounds/'+ bgm[Math.floor(Math.random() * bgm.length)] + ')',
    });
}
