(function () {
  "use strict";
  var body = document.body;
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");

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
    document.addEventListener("click", function (event) {
      if (body.classList.contains("nav-open") && !event.target.closest(".nav-pill")) closeNavigation();
    });
  }

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealItems = document.querySelectorAll(".reveal");

  function formatNumber(value) {
    return String(Math.round(value)).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  }

  function runCounter(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1400;
    var start = null;
    function step(timestamp) {
      if (start === null) start = timestamp;
      var progress = Math.min(1, (timestamp - start) / duration);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = prefix + formatNumber(target * eased) + suffix;
      if (progress < 1) window.requestAnimationFrame(step);
    }
    window.requestAnimationFrame(step);
  }

  if (!reduceMotion && "IntersectionObserver" in window) {
    document.documentElement.classList.add("motion-ok");
    var seenCounters = new WeakSet();
    var observer = new IntersectionObserver(function (entries) {
      for (var j = 0; j < entries.length; j += 1) {
        if (!entries[j].isIntersecting) continue;
        var el = entries[j].target;
        el.classList.add("is-visible");
        var nums = el.querySelectorAll("[data-count]");
        for (var n = 0; n < nums.length; n += 1) {
          if (!seenCounters.has(nums[n])) { seenCounters.add(nums[n]); runCounter(nums[n]); }
        }
        observer.unobserve(el);
      }
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.15 });
    for (var k = 0; k < revealItems.length; k += 1) observer.observe(revealItems[k]);
  }

  var printButton = document.querySelector("[data-print-resume]");
  if (printButton) printButton.addEventListener("click", function () { window.print(); });
})();
