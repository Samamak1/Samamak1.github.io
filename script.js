(function () {
  "use strict";

  var body = document.body;
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var progress = document.querySelector(".scroll-progress span");
  var years = document.querySelectorAll("[data-year]");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  for (var y = 0; y < years.length; y += 1) {
    years[y].textContent = String(new Date().getFullYear());
  }

  function closeNavigation() {
    body.classList.remove("nav-open");
    if (toggle) toggle.setAttribute("aria-expanded", "false");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    var links = nav.querySelectorAll("a");
    for (var i = 0; i < links.length; i += 1) links[i].addEventListener("click", closeNavigation);
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeNavigation();
    });
  }

  function updateProgress() {
    if (!progress) return;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var value = max > 0 ? Math.min(100, Math.max(0, (window.scrollY / max) * 100)) : 0;
    progress.style.width = value + "%";
  }
  updateProgress();
  window.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress);

  var revealItems = document.querySelectorAll(".reveal");
  if (!reduceMotion && "IntersectionObserver" in window && revealItems.length) {
    document.documentElement.classList.add("reveal-ready");
    var observer = new IntersectionObserver(function (entries) {
      for (var j = 0; j < entries.length; j += 1) {
        if (entries[j].isIntersecting) {
          entries[j].target.classList.add("is-visible");
          observer.unobserve(entries[j].target);
        }
      }
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.08 });
    for (var k = 0; k < revealItems.length; k += 1) observer.observe(revealItems[k]);
  }

  var printButton = document.querySelector("[data-print-resume]");
  if (printButton) printButton.addEventListener("click", function () { window.print(); });
})();
