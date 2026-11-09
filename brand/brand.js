(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* toast + copy */
  var toastEl = $('#toast'), tt;
  function toast(m) { toastEl.textContent = m; toastEl.classList.add('on'); clearTimeout(tt); tt = setTimeout(function () { toastEl.classList.remove('on'); }, 1800); }
  function copy(t) {
    var done = function () { toast('Copied ' + t); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(done, done); else done();
  }

  /* rail: active chapter, progress, phone menu */
  var links = $$('#railList a'), secs = links.map(function (a) { return $(a.getAttribute('href')); });
  function setOn(id) { links.forEach(function (a) { var on = a.getAttribute('href') === '#' + id; a.classList.toggle('on', on); if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); }); }
  function onScroll() {
    var y = window.scrollY + window.innerHeight * 0.35, cur = secs[0].id;
    secs.forEach(function (s) { if (s.offsetTop <= y) cur = s.id; });
    setOn(cur);
    var h = document.documentElement.scrollHeight - window.innerHeight;
    $('#prog').style.width = (h > 0 ? Math.min(100, window.scrollY / h * 100) : 0) + '%';
  }
  window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('resize', onScroll); onScroll();
  var rail = $('#rail'), mb = $('#menuBtn');
  mb.addEventListener('click', function () { var o = rail.classList.toggle('open'); mb.setAttribute('aria-expanded', o); });
  links.forEach(function (a) { a.addEventListener('click', function () { rail.classList.remove('open'); mb.setAttribute('aria-expanded', 'false'); }); });

  /* reveal (70 ms apart, as on the site) */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      var n = 0;
      es.forEach(function (e) { if (e.isIntersecting) { e.target.style.transitionDelay = (n++ * 70) + 'ms'; e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px' });
    $$('.reveal').forEach(function (el) { io.observe(el); });
    setTimeout(function () { $$('.reveal').forEach(function (el) { el.classList.add('in'); }); }, 4000);
  } else $$('.reveal').forEach(function (el) { el.classList.add('in'); });

  /* colour */
  function hexRgb(h) { h = h.replace('#', ''); return [0, 2, 4].map(function (i) { return parseInt(h.substr(i, 2), 16); }); }
  function lum(rgb) { var a = rgb.map(function (v) { v /= 255; return v <= .04045 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * a[0] + .7152 * a[1] + .0722 * a[2]; }
  function ratio(a, b) { var l1 = lum(hexRgb(a)), l2 = lum(hexRgb(b)), hi = Math.max(l1, l2), lo = Math.min(l1, l2); return (hi + .05) / (lo + .05); }
  function cmyk(rgb) {
    var r = rgb[0] / 255, g = rgb[1] / 255, b = rgb[2] / 255, k = 1 - Math.max(r, g, b);
    if (k >= 1) return [0, 0, 0, 100];
    return [(1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k].map(function (v) { return Math.round(v * 100); });
  }
  function cards(list) {
    return list.map(function (c) {
      var r = hexRgb(c[1]), k = cmyk(r);
      return '<button class="swc" data-copy="' + c[1] + '" aria-label="Copy ' + c[0] + ' ' + c[1] + '"><div class="chip" style="background:' + c[1] + '"></div><div class="inf"><b>' + c[0] + '</b><small>' + c[2] + '</small><code>HEX ' + c[1] + '<br>RGB ' + r.join(' ') + '<br>CMYK ' + k.join(' ') + '</code></div></button>';
    }).join('');
  }
  var core = [
    ['Brand Blue', '#3167CA', 'Logo, primary buttons, links, the marked phrase.'],
    ['Navy', '#1E4691', 'Hover, pressed, dark bands.'],
    ['Ink', '#1F1F3D', 'Headings and strong text.'],
    ['Wash', '#EAF0FB', 'Tinted grounds and tags.'],
    ['White', '#FFFFFF', 'The page. Light only.']
  ];
  var more = [
    ['Deep navy', '#0F2350', 'Start of the dark gradient.'],
    ['Sky', '#6FA0F5', 'Hover borders, arrows, glows.'],
    ['Mist', '#DDE7F8', 'Borders on blue, focus halo.'],
    ['Body', '#4C4C63', 'Paragraphs.'],
    ['Muted', '#62627A', 'Captions and labels.'],
    ['Line', '#E7E4E9', 'Hairlines and card borders.'],
    ['Alt paper', '#FAF9FB', 'Alternate sections.'],
    ['OK', '#137A4A', 'Success and done states.'],
    ['Amber', '#A96B00', 'Notes and Sample data chips.'],
    ['Red', '#D93A30', 'Errors and deadline alerts.'],
    ['Yellow', '#FFD23F', 'Highlight on blue grounds only.'],
    ['Odoo plum', '#714B67', 'Odoo things only.']
  ];
  $('#swatches').innerHTML = cards(core);
  $('#swatches2').innerHTML = cards(more);
  $$('.sw').forEach(function (s) { s.addEventListener('click', function (e) { var b = e.target.closest('[data-copy]'); if (b) copy(b.dataset.copy); }); });
  var pairs = [
    ['Brand Blue on white', '#3167CA', '#FFFFFF'],
    ['White on Brand Blue', '#FFFFFF', '#3167CA'],
    ['Ink on white', '#1F1F3D', '#FFFFFF'],
    ['Body on white', '#4C4C63', '#FFFFFF'],
    ['Muted on white', '#62627A', '#FFFFFF'],
    ['Navy on Wash', '#1E4691', '#EAF0FB'],
    ['Amber on amber tint', '#A96B00', '#FDF6E9'],
    ['Yellow on Navy', '#FFD23F', '#1E4691'],
    ['Sky on white (never text)', '#6FA0F5', '#FFFFFF'],
    ['Old grey #8888A0 on white', '#8888A0', '#FFFFFF']
  ];
  $('#contrast').innerHTML = pairs.map(function (p) {
    var r = ratio(p[1], p[2]);
    var cls = r >= 4.5 ? 'p' : r >= 3 ? 'l' : 'f';
    var lab = r >= 7 ? 'AAA' : r >= 4.5 ? 'AA' : r >= 3 ? 'Large only' : 'Fails';
    return '<div class="cx"><div class="s" style="background:' + p[2] + ';color:' + p[1] + '">Aa <span>' + p[0] + '</span></div><div class="m"><span>' + p[1] + ' on ' + p[2] + '<br><b>' + r.toFixed(2) + ' : 1</b></span><span class="badge ' + cls + '">' + lab + '</span></div></div>';
  }).join('');

  /* taglines */
  var tl = $('#tlLine'), tabs = $$('#tlTabs button');
  tabs.forEach(function (b, i) {
    b.addEventListener('click', function () { tabs.forEach(function (x) { x.setAttribute('aria-selected', x === b); }); tl.innerHTML = b.dataset.t.replace(/&lt;/g, '<').replace(/&gt;/g, '>'); });
    b.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); var n = tabs[(i + (e.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length]; n.focus(); n.click(); }
    });
  });

  /* type tester */
  var tx = $('#tt'), ts = $('#ts'), tw = $('#tw');
  function apply() {
    var w = tw.value.split('|');
    tx.style.fontFamily = w[0]; tx.style.fontWeight = w[1]; tx.style.letterSpacing = w[2]; tx.style.fontSize = ts.value + 'px'; $('#to').textContent = ts.value + ' px';
  }
  ts.addEventListener('input', apply); tw.addEventListener('change', apply);
  tx.addEventListener('input', function () { tx.style.height = 'auto'; tx.style.height = tx.scrollHeight + 'px'; });

  /* image filter + lightbox */
  var pf = $$('#pf button'), tiles = $$('#pg .tile');
  pf.forEach(function (b) {
    b.addEventListener('click', function () {
      pf.forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      tiles.forEach(function (t) { t.hidden = !(b.dataset.f === 'all' || t.dataset.cat === b.dataset.f); });
    });
  });
  var lb = $('#lb'), lbImg = $('#lbImg'), lbCap = $('#lbCap'), last;
  function open(src, cap, from) {
    lbImg.src = src; lbImg.alt = cap; lbCap.textContent = cap; last = from;
    if (lb.showModal) lb.showModal(); else lb.setAttribute('open', '');
  }
  tiles.forEach(function (t) { t.addEventListener('click', function () { open(t.dataset.src, t.dataset.cap, t); }); });
  $$('img[data-zoom]').forEach(function (im) {
    im.tabIndex = 0;
    im.addEventListener('click', function () { open(im.dataset.zoom, im.dataset.cap || im.alt, im); });
    im.addEventListener('keydown', function (e) { if (e.key === 'Enter') open(im.dataset.zoom, im.dataset.cap || im.alt, im); });
  });
  $('#lbX').addEventListener('click', function () { lb.close(); });
  lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  lb.addEventListener('close', function () { if (last && last.focus) last.focus(); });

  /* easing demo */
  var dots = $$('.dot[data-e]');
  function run() {
    dots.forEach(function (d) {
      var w = d.parentNode.clientWidth - 22;
      d.style.transition = 'none'; d.style.transform = 'translateX(0)'; void d.offsetWidth;
      d.style.transition = 'transform ' + (+d.dataset.d * 2) + 'ms ' + d.dataset.e; d.style.transform = 'translateX(' + w + 'px)';
    });
  }
  if (!reduce && 'IntersectionObserver' in window) {
    var started = false, eo = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting && !started) { started = true; run(); setInterval(run, 2800); }
    }); eo.observe($('#eases'));
  } else dots.forEach(function (d) { d.style.transform = 'translateX(' + (d.parentNode.clientWidth - 22) + 'px)'; });
})();
