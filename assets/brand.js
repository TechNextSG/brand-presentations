/* Brand books: the shared kit. Load after deck.js (and motion.js), before a brand's own script.
   - .sw[data-hex]        a colour swatch: click copies the hex; contrast against white and the brand's ink is measured and labelled
   - .lg-stage            a logo on a ground: .lg-bgs buttons [data-bg] swap the ground, [data-guide] toggles the clear-space guides
   - .ts                  a type tester: [data-w] weight buttons, [data-size] range, an editable sample line
   - .bk-zoom             a picture that opens large inside the stage on click (Esc or a click closes it)
   - .bk-flip             a card that turns over on click (voice: say this / not this)
   - [data-tab-group]     tabs that show one [data-pane] at a time
   Every widget paints its finished state at load, so print and the overview need no settle hooks. */
(function () {
  'use strict';
  var $$ = function (sel, root) { return [].slice.call((root || document).querySelectorAll(sel)); };
  var stage = document.querySelector('.stage');

  /* ---------------------------------------------------------------- toast */
  var toast = document.createElement('div'); toast.className = 'bk-toast'; toast.setAttribute('role', 'status');
  (stage || document.body).appendChild(toast);
  var tt = 0;
  function say(msg) { toast.textContent = msg; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 1600); }
  function copy(text, msg) {
    var done = function () { say(msg || ('Copied ' + text)); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () { fallback(); });
    else fallback();
    function fallback() { var t = document.createElement('textarea'); t.value = text; document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (e) {} t.remove(); done(); }
  }
  window.BK = { say: say, copy: copy };

  /* ---------------------------------------------------------------- colour */
  function rgb(hex) { hex = hex.replace('#', ''); if (hex.length === 3) hex = hex.replace(/./g, '$&$&'); var n = parseInt(hex, 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; }
  function lum(hex) { return rgb(hex).map(function (c) { c /= 255; return c <= .03928 ? c / 12.92 : Math.pow((c + .055) / 1.055, 2.4); }).reduce(function (a, c, i) { return a + c * [.2126, .7152, .0722][i]; }, 0); }
  function ratio(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + .05) / (Math.min(x, y) + .05); }
  function grade(r) { return r >= 7 ? 'AAA' : r >= 4.5 ? 'AA' : r >= 3 ? 'AA large' : 'decor only'; }
  BK.ratio = ratio;
  var ink = getComputedStyle(document.body).getPropertyValue('--bk-ink').trim() || '#1F1F3D';
  $$('.sw[data-hex]').forEach(function (s) {
    var hex = s.dataset.hex.toUpperCase();
    s.style.setProperty('--c', hex);
    var chip = s.querySelector('.sw-chip');
    if (chip && !s.classList.contains('sw-light') && lum(hex) > .6) s.classList.add('sw-light');
    var c = s.querySelector('.sw-c');
    if (c) {
      var host = s.closest('[data-ink]'), bi = host ? host.dataset.ink : ink, w = ratio(hex, '#FFFFFF'), k = ratio(hex, bi);
      c.innerHTML = '<span title="This colour against white">white <b>' + w.toFixed(1) + '</b> ' + grade(w) + '</span>' +
        '<span title="This colour against the brand ink ' + bi + '">ink <b>' + k.toFixed(1) + '</b> ' + grade(k) + '</span>';
    }
    var r = s.querySelector('.sw-rgb');
    if (r) r.textContent = 'RGB ' + rgb(hex).join(' ');
    s.setAttribute('role', 'button'); s.setAttribute('tabindex', '0');
    s.setAttribute('aria-label', (s.querySelector('b') ? s.querySelector('b').textContent + ' ' : '') + hex + ', copy');
    var go = function () { copy(hex, 'Copied ' + hex); s.classList.remove('is-copied'); void s.offsetWidth; s.classList.add('is-copied'); };
    s.addEventListener('click', go);
    s.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
  });
  $$('[data-copy]').forEach(function (b) { b.setAttribute('data-i', ''); b.addEventListener('click', function () { copy(b.dataset.copy); }); });

  /* ---------------------------------------------------------------- logo stages */
  $$('.lg-wrap').forEach(function (w) {
    var st = w.querySelector('.lg-stage');
    $$('.lg-bgs [data-bg]', w).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('.lg-bgs [data-bg]', w).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        st.dataset.bg = b.dataset.bg;
        $$('.lg-img', st).forEach(function (im) { var on = (im.dataset.on || 'light dark brand photo').split(' ').indexOf(b.dataset.bg) >= 0; im.hidden = !on; });
      });
    });
    var g = w.querySelector('[data-guide]');
    if (g) g.addEventListener('click', function () { var on = st.classList.toggle('is-guides'); g.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    var first = w.querySelector('.lg-bgs [aria-pressed="true"]') || w.querySelector('.lg-bgs [data-bg]');
    if (first) first.click();
  });

  /* ---------------------------------------------------------------- type tester */
  $$('.ts').forEach(function (t) {
    var line = t.querySelector('.ts-line'), out = t.querySelector('.ts-px'), rng = t.querySelector('[data-size]');
    $$('[data-w]', t).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-w]', t).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        line.style.fontWeight = b.dataset.w;
        if (b.dataset.style) line.style.fontStyle = b.dataset.style; else line.style.fontStyle = '';
      });
    });
    if (rng) {
      var set = function () { line.style.fontSize = rng.value + 'px'; if (out) out.textContent = rng.value + ' px'; };
      rng.addEventListener('input', set); set();
      rng.addEventListener('keydown', function (e) { e.stopPropagation(); });
    }
    if (line) {
      line.setAttribute('contenteditable', 'true'); line.setAttribute('spellcheck', 'false'); line.setAttribute('data-i', '');
      line.addEventListener('keydown', function (e) { e.stopPropagation(); if (e.key === 'Escape' || e.key === 'Enter') { e.preventDefault(); line.blur(); } });
    }
  });

  /* ---------------------------------------------------------------- tabs */
  $$('[data-tab-group]').forEach(function (g) {
    var tabs = $$('[data-tab]', g), panes = $$('[data-pane]', g);
    function show(k) {
      tabs.forEach(function (t) { t.setAttribute('aria-pressed', t.dataset.tab === k ? 'true' : 'false'); });
      panes.forEach(function (p) { p.hidden = p.dataset.pane !== k; });
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { show(t.dataset.tab); }); });
    if (tabs[0]) show((g.querySelector('[data-tab][aria-pressed="true"]') || tabs[0]).dataset.tab);
  });

  /* ---------------------------------------------------------------- flip cards */
  $$('.bk-flip').forEach(function (c) {
    c.setAttribute('role', 'button'); c.setAttribute('tabindex', '0'); c.setAttribute('data-i', '');
    var go = function () { c.classList.toggle('is-flipped'); };
    c.addEventListener('click', go);
    c.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
  });


  /* ---------------------------------------------------------------- jump links ([data-go] = a slide id) */
  if (stage) stage.addEventListener('click', function (e) {
    var a = e.target.closest('[data-go]'); if (!a || !window.Deck) return;
    e.preventDefault(); e.stopPropagation(); Deck.goId(a.dataset.go);
  });

  /* ---------------------------------------------------------------- motion curves: .ez rows play a dot along a track with their curve */
  $$('.ez').forEach(function (z) {
    z.setAttribute('data-i', ''); z.setAttribute('role', 'button'); z.setAttribute('tabindex', '0');
    var go = function () { z.classList.remove('is-run'); void z.offsetWidth; z.classList.add('is-run'); };
    z.addEventListener('click', go);
    z.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); go(); } });
  });


  /* ---------------------------------------------------------------- pointer-origin fills (.hb-btn, .bhd-btn): --x/--y in % of the button */
  $$('.hb-btn, .bhd-btn').forEach(function (b) {
    b.setAttribute('data-i', '');
    b.addEventListener('pointerenter', at); b.addEventListener('pointermove', at);
    function at(e) { var r = b.getBoundingClientRect(); b.style.setProperty('--x', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%'); b.style.setProperty('--y', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%'); }
  });

  /* ---------------------------------------------------------------- TRE tremor field: fine lines that tremble where the pointer passes, then settle */
  $$('.tre-field').forEach(function (f) {
    var cv = document.createElement('canvas'); f.prepend(cv); cv.style.zIndex = 1;
    var W = 0, H = 0, dpr = 1, px = -999, py = -999, energy = 0, t0 = performance.now(), raf = 0;
    function size() { var r = f.getBoundingClientRect(), sc = (window.Deck && Deck.scale) || 1; W = f.offsetWidth; H = f.offsetHeight; dpr = Math.min(2, (window.devicePixelRatio || 1) * sc); cv.width = W * dpr; cv.height = H * dpr; }
    function draw(t) {
      var c = cv.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, W, H);
      var n = 26, gap = H / (n + 1);
      for (var i = 1; i <= n; i++) {
        var y0 = i * gap; c.beginPath();
        for (var x = W * .38; x <= W; x += 6) {
          var d = Math.hypot(x - px, y0 - py), k = Math.max(0, 1 - d / 190) * energy;
          var y = y0 + Math.sin(x * .045 + t * .004 + i) * (1.2 + k * 14) * (0.4 + .6 * Math.sin(i * 1.7 + x * .002));
          if (x === W * .38) c.moveTo(x, y); else c.lineTo(x, y);
        }
        var a = Math.min(1, (W - W * .38) / W) * .55;
        c.strokeStyle = i % 3 ? 'rgba(201,164,92,' + a + ')' : 'rgba(139,107,69,' + (a + .1) + ')'; c.lineWidth = 1.1; c.stroke();
      }
    }
    function loop(now) { energy *= .965; draw(now - t0); if (f.closest('.slide.is-active')) raf = requestAnimationFrame(loop); else raf = 0; }
    function kick() { if (!raf) raf = requestAnimationFrame(loop); }
    f.addEventListener('pointermove', function (e) { var r = f.getBoundingClientRect(); px = (e.clientX - r.left) / r.width * W; py = (e.clientY - r.top) / r.height * H; energy = Math.min(1, energy + .12); kick(); });
    f.addEventListener('pointerleave', function () { px = py = -999; });
    size(); draw(0);
    if (stage) document.querySelector('.deck').addEventListener('deck:slide', function () { setTimeout(function () { size(); if (f.closest('.slide.is-active') && !(window.Deck && Deck.print)) kick(); else draw(0); }, 60); });
    addEventListener('resize', function () { size(); draw(0); });
  });

  /* ---------------------------------------------------------------- zoom */
  var box = document.createElement('div'); box.className = 'bk-lb'; box.setAttribute('aria-hidden', 'true');
  box.innerHTML = '<figure><img alt=""><figcaption></figcaption></figure><button type="button" class="bk-lb-x" aria-label="Close">&times;</button>';
  (stage || document.body).appendChild(box);
  function close() { box.classList.remove('on'); box.setAttribute('aria-hidden', 'true'); }
  box.addEventListener('click', function (e) { e.stopPropagation(); close(); });
  document.addEventListener('keydown', function (e) { if (box.classList.contains('on') && (e.key === 'Escape' || e.key === 'z')) { e.preventDefault(); e.stopPropagation(); close(); } }, true);
  $$('.bk-zoom').forEach(function (el) {
    el.setAttribute('data-i', ''); el.setAttribute('role', 'button'); el.setAttribute('tabindex', '0');
    var open = function () {
      var im = el.tagName === 'IMG' ? el : el.querySelector('img');
      box.querySelector('img').src = el.dataset.full || im.currentSrc || im.src;
      box.querySelector('figcaption').textContent = el.dataset.cap || im.alt || '';
      box.classList.add('on'); box.setAttribute('aria-hidden', 'false');
    };
    el.addEventListener('click', open);
    el.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); open(); } });
  });
  if (window.Deck && Deck.print) document.body.classList.add('bk-print');
  addEventListener('beforeprint', function () { document.body.classList.add('bk-print'); });
  addEventListener('afterprint', function () { if (!(window.Deck && Deck.print)) document.body.classList.remove('bk-print'); });
  if (window.Deck && Deck.on) document.querySelector('.deck').addEventListener('deck:slide', close);
})();
