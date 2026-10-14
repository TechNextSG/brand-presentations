/* Brand kits: swatches that copy and measure contrast, logo grounds and clear space, type testers, motion curves,
   pointer-fill buttons, the TRE tremor field, zoom, and the section nav. */
(function () {
  'use strict';
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };

  var toast = document.createElement('div'); toast.className = 'toast'; toast.setAttribute('role', 'status'); document.body.appendChild(toast);
  var tt = 0;
  function say(m) { toast.textContent = m; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 1500); }
  function copy(t) {
    var ok = function () { say('Copied ' + t); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, fb); else fb();
    function fb() { var a = document.createElement('textarea'); a.value = t; document.body.appendChild(a); a.select(); try { document.execCommand('copy'); } catch (e) {} a.remove(); ok(); }
  }

  /* colour */
  function rgb(h) { h = h.replace('#', ''); var n = parseInt(h, 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; }
  function lum(h) { return rgb(h).map(function (c) { c /= 255; return c <= .03928 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4); }).reduce(function (a, c, i) { return a + c * [.2126, .7152, .0722][i]; }, 0); }
  function ratio(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }
  function grade(r) { return r >= 7 ? 'AAA' : r >= 4.5 ? 'AA' : r >= 3 ? 'AA large' : 'decor only'; }
  $$('.sw[data-hex]').forEach(function (s) {
    var hex = s.dataset.hex.toUpperCase(); s.style.setProperty('--c', hex);
    if (lum(hex) > .6) s.classList.add('sw-light');
    var host = s.closest('[data-ink]'), ink = host ? host.dataset.ink : '#1F1F3D';
    var c = s.querySelector('.sw-c'), r = s.querySelector('.sw-rgb');
    if (c) { var w = ratio(hex, '#FFFFFF'), k = ratio(hex, ink); c.innerHTML = '<span>white <b>' + w.toFixed(1) + '</b> ' + grade(w) + '</span><span>ink <b>' + k.toFixed(1) + '</b> ' + grade(k) + '</span>'; }
    if (r) r.textContent = 'RGB ' + rgb(hex).join(' ');
    s.setAttribute('aria-label', (s.querySelector('b') ? s.querySelector('b').textContent + ' ' : '') + hex + ', copy');
    s.addEventListener('click', function () { copy(hex); s.classList.remove('is-copied'); void s.offsetWidth; s.classList.add('is-copied'); });
  });

  /* logo grounds */
  $$('.lg-wrap').forEach(function (w) {
    var st = w.querySelector('.lg-stage');
    $$('.lg-bgs [data-bg]', w).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('.lg-bgs [data-bg]', w).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        st.dataset.bg = b.dataset.bg;
        $$('.lg-img', st).forEach(function (im) { im.hidden = (im.dataset.on || '').split(' ').indexOf(b.dataset.bg) < 0; });
      });
    });
    var g = w.querySelector('[data-guide]');
    if (g) g.addEventListener('click', function () { g.setAttribute('aria-pressed', st.classList.toggle('is-guides') ? 'true' : 'false'); });
    var f = w.querySelector('.lg-bgs [aria-pressed="true"]'); if (f) f.click();
  });

  /* type testers */
  $$('.ts').forEach(function (t) {
    var line = t.querySelector('.ts-line'), out = t.querySelector('.ts-px'), rng = t.querySelector('[data-size]');
    $$('[data-w]', t).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-w]', t).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        line.style.fontWeight = b.dataset.w; line.style.fontStyle = b.dataset.style || '';
      });
    });
    var on = t.querySelector('[data-w][aria-pressed="true"]'); if (on) on.click();
    if (rng) { var set = function () { line.style.fontSize = rng.value + 'px'; if (out) out.textContent = rng.value + ' px'; }; rng.addEventListener('input', set); set(); }
    line.setAttribute('contenteditable', 'true'); line.setAttribute('spellcheck', 'false');
  });

  /* motion curves */
  $$('.ez').forEach(function (z) { z.addEventListener('click', function () { z.classList.remove('is-run'); void z.offsetWidth; z.classList.add('is-run'); }); });

  /* pointer-origin fills (HummingBeing, BHD Asia buttons) */
  $$('.hb-btn, .bhd-btn').forEach(function (b) {
    function at(e) { var r = b.getBoundingClientRect(); b.style.setProperty('--x', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%'); b.style.setProperty('--y', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%'); }
    b.addEventListener('pointerenter', at); b.addEventListener('pointermove', at);
  });

  /* TRE tremor field: lines tremble where the pointer passes, then settle */
  $$('.tre-field').forEach(function (f) {
    var cv = document.createElement('canvas'); cv.style.zIndex = 1; f.prepend(cv);
    var W, H, dpr, px = -999, py = -999, en = 0, raf = 0, t0 = performance.now();
    function size() { W = f.offsetWidth; H = f.offsetHeight; dpr = Math.min(2, window.devicePixelRatio || 1); cv.width = W * dpr; cv.height = H * dpr; }
    function draw(t) {
      var c = cv.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, W, H);
      var n = 18, gap = H / (n + 1), x0 = W * .38;
      for (var i = 1; i <= n; i++) {
        var y0 = i * gap; c.beginPath();
        for (var x = x0; x <= W; x += 6) {
          var k = Math.max(0, 1 - Math.hypot(x - px, y0 - py) / 160) * en;
          var y = y0 + Math.sin(x * .045 + t * .004 + i) * (1 + k * 12) * (.4 + .6 * Math.sin(i * 1.7 + x * .002));
          if (x === x0) c.moveTo(x, y); else c.lineTo(x, y);
        }
        c.strokeStyle = i % 3 ? 'rgba(201,164,92,.55)' : 'rgba(139,107,69,.65)'; c.lineWidth = 1; c.stroke();
      }
    }
    function loop(now) { en *= .965; draw(now - t0); raf = en > .01 ? requestAnimationFrame(loop) : 0; }
    f.addEventListener('pointermove', function (e) { var r = f.getBoundingClientRect(); px = e.clientX - r.left; py = e.clientY - r.top; en = Math.min(1, en + .12); if (!raf) raf = requestAnimationFrame(loop); });
    size(); draw(0); addEventListener('resize', function () { size(); draw(0); });
  });

  /* zoom */
  var lb = document.createElement('div'); lb.className = 'lb'; lb.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure>'; document.body.appendChild(lb);
  lb.addEventListener('click', function () { lb.classList.remove('on'); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('on'); });
  $$('.zoom').forEach(function (el) {
    el.addEventListener('click', function () {
      var im = el.tagName === 'IMG' ? el : el.querySelector('img');
      lb.querySelector('img').src = im.currentSrc || im.src; lb.querySelector('figcaption').textContent = el.dataset.cap || im.alt || '';
      lb.classList.add('on');
    });
  });

  /* section nav follows the scroll */
  var links = $$('.side a[href^="#"]');
  if (links.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + en.target.id); }); });
    }, { rootMargin: '-80px 0px -70% 0px' });
    $$('.sec').forEach(function (s) { io.observe(s); });
  }
})();
