/* starfield.js — subtle p5.js cosmic backdrop for the hero.
 *
 * 🇨🇿 Decentní hvězdné pozadí (instance mode, scoped na #starfield-host).
 *     Respektuje prefers-reduced-motion (statický render, žádná smyčka).
 *     Bez p5 nebo bez host elementu se tiše vypne — žádné console errory.
 */
(function () {
  if (!window.p5) return;
  var host = document.getElementById('starfield-host');
  if (!host) return;

  var reduce =
    window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // eslint-disable-next-line no-new
  new window.p5(function (p) {
    var stars = [];

    function seed(w, h) {
      stars = [];
      var count = Math.min(170, Math.floor((w * h) / 8500));
      for (var i = 0; i < count; i++) {
        stars.push({
          x: p.random(w),
          y: p.random(h),
          r: p.random(0.4, 1.7),
          base: p.random(45, 180),
          tw: p.random(0.003, 0.02),
          ph: p.random(p.TWO_PI),
          gold: p.random() < 0.08,
          vy: p.random(0.02, 0.1),
        });
      }
    }

    p.setup = function () {
      var c = p.createCanvas(host.offsetWidth, host.offsetHeight);
      c.parent(host);
      p.clear();
      seed(p.width, p.height);
      if (reduce) {
        p.noLoop();
        p.redraw();
      }
    };

    p.windowResized = function () {
      p.resizeCanvas(host.offsetWidth, host.offsetHeight);
      seed(p.width, p.height);
      if (reduce) p.redraw();
    };

    p.draw = function () {
      p.clear();
      p.noStroke();
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        var tw = reduce ? 1 : 0.6 + 0.4 * Math.sin(s.ph);
        var a = s.base * tw;
        if (s.gold) p.fill(212, 165, 116, a);
        else p.fill(248, 248, 248, a);
        p.circle(s.x, s.y, s.r * 2);
        if (!reduce) {
          s.ph += s.tw;
          s.y += s.vy;
          if (s.y > p.height + 2) {
            s.y = -2;
            s.x = p.random(p.width);
          }
        }
      }
    };
  });
})();
