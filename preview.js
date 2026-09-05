document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a.zoom-link');
  if (!links.length) return;
  const dialog = document.createElement('dialog');
  dialog.className = 'image-dialog';
  dialog.setAttribute('aria-label', 'Project image');
  dialog.innerHTML = '<header><a target="_blank" rel="noopener">Open original image</a><button type="button">Close</button></header><img alt="">';
  document.body.append(dialog);
  const img = dialog.querySelector('img');
  const original = dialog.querySelector('a');
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
  links.forEach(link => link.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    img.src = link.href;
    img.alt = link.querySelector('img')?.alt || 'Project image';
    original.href = link.href;
    dialog.showModal();
  }));
});

// Portfolio-only motion. Other review pages and the resume keep their behavior.
(function () {
  'use strict';
  if (!document.body.matches('body.home, body.detail')) return;

  const header = document.querySelector('.site-header');
  let framePending = false;
  function updateHeader() {
    if (header) header.classList.toggle('header-scrolled', window.scrollY > 20);
    framePending = false;
  }
  updateHeader();
  window.addEventListener('scroll', () => {
    if (!framePending) {
      framePending = true;
      window.requestAnimationFrame(updateHeader);
    }
  }, { passive: true });

  const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  const targets = Array.from(document.querySelectorAll(
    '.career-card, .project-card, .section-head, .experience-grid > div, .tool-groups > div, .detail-body > section'
  ));
  let observer;
  const reveal = element => {
    element.classList.remove('is-pending');
    element.classList.add('is-shown');
    if (observer) observer.unobserve(element);
  };
  const revealAll = () => {
    targets.forEach(reveal);
    if (observer) observer.disconnect();
  };

  if (!motionPreference.matches && 'IntersectionObserver' in window) {
    try {
      observer = new IntersectionObserver(entries => {
        entries.forEach(entry => { if (entry.isIntersecting) reveal(entry.target); });
      }, { rootMargin: '0px 0px 32px 0px', threshold: 0.04 });
      targets.forEach(element => {
        // Never conceal content already visible on load or deep-link navigation.
        if (element.getBoundingClientRect().top >= window.innerHeight) {
          element.classList.add('portfolio-enter', 'is-pending');
          observer.observe(element);
        }
      });
    } catch (_) {
      revealAll();
    }
  }
  if (motionPreference.addEventListener) {
    motionPreference.addEventListener('change', event => { if (event.matches) revealAll(); });
  }
  document.addEventListener('focusin', event => {
    const target = event.target.closest('.portfolio-enter');
    if (target) reveal(target);
  });
  window.addEventListener('beforeprint', revealAll);
  window.addEventListener('pageshow', event => { if (event.persisted) revealAll(); });
})();
