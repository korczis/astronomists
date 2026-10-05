/* enhance.js — progressive-enhancement failsafe.
 *
 * 🇨🇿 Pojistka pro scroll-reveal: pokud Alpine (CDN) selže nebo se nenačte,
 *     obsah se i tak zobrazí. Reveal-skrytí je v CSS gated na html.js — tady
 *     jen garantujeme, že nic nezůstane neviditelné.
 */
(function () {
  function showAll() {
    var els = document.querySelectorAll('.reveal:not(.is-in)');
    for (var i = 0; i < els.length; i++) els[i].classList.add('is-in');
  }

  window.addEventListener('load', function () {
    // Alpine boots on DOMContentLoaded; if it never registered, reveal manually.
    window.setTimeout(function () {
      if (!window.Alpine) showAll();
    }, 800);
  });
})();
