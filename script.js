// Reveal-on-scroll: opacity/transform only, honors prefers-reduced-motion.
// Fails open: if anything goes wrong, all content is revealed.
(function () {
  var els = document.querySelectorAll('.reveal');
  function showAll() {
    for (var i = 0; i < els.length; i++) { els[i].classList.add('is-in'); }
  }
  try {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || !('IntersectionObserver' in window)) { showAll(); return; }
    var io = new IntersectionObserver(function (entries) {
      for (var i = 0; i < entries.length; i++) {
        if (entries[i].isIntersecting) {
          entries[i].target.classList.add('is-in');
          io.unobserve(entries[i].target);
        }
      }
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    for (var j = 0; j < els.length; j++) { io.observe(els[j]); }
    // Safety net: whatever happens, nothing stays hidden for long.
    setTimeout(showAll, 2500);
  } catch (e) {
    showAll();
  }
})();
