/* StoryMe — site behaviour (no dependencies) */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Mobile menu ---------- */
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-toggle');
  if (header && toggle) {
    toggle.addEventListener('click', function () {
      var open = header.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && header.classList.contains('is-open')) {
        header.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---------- Starfields ---------- */
  function seeded(seed) {
    var x = seed || 1;
    return function () { x = (x * 9301 + 49297) % 233280; return x / 233280; };
  }
  document.querySelectorAll('.starfield').forEach(function (field, i) {
    var count = parseInt(field.getAttribute('data-stars') || '70', 10);
    if (window.innerWidth < 700) count = Math.round(count * 0.5);
    var rnd = seeded(17 + i * 31);
    var frag = document.createDocumentFragment();
    for (var n = 0; n < count; n++) {
      var s = document.createElement('span');
      var size = (1 + rnd() * 2.6).toFixed(1);
      s.className = 'star';
      s.style.left = (rnd() * 100).toFixed(2) + '%';
      s.style.top = (rnd() * 100).toFixed(2) + '%';
      s.style.width = size + 'px';
      s.style.height = size + 'px';
      s.style.animationDelay = (rnd() * 3.6).toFixed(2) + 's';
      s.style.animationDuration = (2.8 + rnd() * 2.4).toFixed(2) + 's';
      frag.appendChild(s);
    }
    field.appendChild(frag);
  });

  /* ---------- Scroll reveal ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Hero sparkles around the glow ---------- */
  var art = document.querySelector('[data-sparkles]');
  if (art && !reduceMotion) initSparkles(art);

  function initSparkles(wrap) {
    var img = wrap.querySelector('img');
    var canvas = wrap.querySelector('.sparkle-canvas');
    if (!img || !canvas) return;
    var ctx = canvas.getContext('2d');
    // Source image is 1672 x 941. Glow hotspots, in source pixels.
    var NW = 1672, NH = 941;
    var body = { x: 800, y: 470, rx: 215, ry: 330 };   // the glowing child
    var wand = { x: 1000, y: 605 };                     // wand tip
    var trail = [[640, 560], [700, 720], [780, 800], [900, 700], [980, 640], [720, 250], [860, 200]];
    var particles = [];
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var map = { s: 1, ox: 0, oy: 0 };
    var running = false, visible = true, raf = 0;

    function layout() {
      var r = wrap.getBoundingClientRect();
      canvas.width = Math.round(r.width * dpr);
      canvas.height = Math.round(r.height * dpr);
      var s = Math.max(r.width / NW, r.height / NH);
      var pos = (getComputedStyle(img).objectPosition || '50% 50%').split(' ');
      var px = parseFloat(pos[0]) / 100, py = parseFloat(pos[1] || pos[0]) / 100;
      if (isNaN(px)) px = 0.5; if (isNaN(py)) py = 0.5;
      map.s = s;
      map.ox = (r.width - NW * s) * px;
      map.oy = (r.height - NH * s) * py;
    }

    function spawn() {
      var sx, sy, roll = Math.random();
      if (roll < 0.28) {                 // from the wand tip
        sx = wand.x + (Math.random() - 0.5) * 40;
        sy = wand.y + (Math.random() - 0.5) * 40;
      } else if (roll < 0.55) {          // along the glowing swirl
        var t = trail[Math.floor(Math.random() * trail.length)];
        sx = t[0] + (Math.random() - 0.5) * 70;
        sy = t[1] + (Math.random() - 0.5) * 70;
      } else {                           // ring around the child
        var a = Math.random() * Math.PI * 2;
        var k = 0.75 + Math.random() * 0.35;
        sx = body.x + Math.cos(a) * body.rx * k;
        sy = body.y + Math.sin(a) * body.ry * k;
      }
      var star = Math.random() < 0.35;
      particles.push({
        x: sx, y: sy,
        vx: (Math.random() - 0.5) * 0.35,
        vy: -0.15 - Math.random() * 0.45,
        life: 0,
        max: 70 + Math.random() * 90,
        size: star ? 5 + Math.random() * 7 : 1.2 + Math.random() * 2.4,
        star: star,
        spin: Math.random() * Math.PI,
        hue: Math.random() < 0.8 ? '255, 214, 110' : '255, 250, 235'
      });
    }

    function drawStar(x, y, r, rot) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rot);
      ctx.beginPath();
      for (var i = 0; i < 4; i++) {
        ctx.lineTo(0, -r);
        ctx.quadraticCurveTo(0, 0, r, 0);
        ctx.rotate(Math.PI / 2);
      }
      ctx.closePath();
      ctx.fill();
      ctx.restore();
    }

    function frame() {
      if (!running) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      var target = window.innerWidth < 700 ? 45 : 90;
      for (var i = 0; i < 3 && particles.length < target; i++) spawn();
      ctx.globalCompositeOperation = 'lighter';
      for (var p = particles.length - 1; p >= 0; p--) {
        var q = particles[p];
        q.life++;
        q.x += q.vx + Math.sin((q.life + q.spin * 40) / 18) * 0.25;
        q.y += q.vy;
        q.spin += 0.02;
        var t = q.life / q.max;
        if (t >= 1) { particles.splice(p, 1); continue; }
        var alpha = t < 0.2 ? t / 0.2 : 1 - (t - 0.2) / 0.8;
        var twinkle = 0.65 + 0.35 * Math.sin(q.life * 0.35 + q.spin * 5);
        var x = (map.ox + q.x * map.s) * dpr;
        var y = (map.oy + q.y * map.s) * dpr;
        var size = q.size * map.s * dpr * 2.3;
        if (q.star) {
          ctx.shadowColor = 'rgba(' + q.hue + ', 0.9)';
          ctx.shadowBlur = 12 * dpr;
          ctx.fillStyle = 'rgba(' + q.hue + ',' + (alpha * twinkle).toFixed(3) + ')';
          drawStar(x, y, size, q.spin);
        } else {
          ctx.shadowBlur = 0;
          var g = ctx.createRadialGradient(x, y, 0, x, y, size * 2.2);
          g.addColorStop(0, 'rgba(' + q.hue + ',' + (alpha * twinkle).toFixed(3) + ')');
          g.addColorStop(1, 'rgba(' + q.hue + ',0)');
          ctx.fillStyle = g;
          ctx.beginPath();
          ctx.arc(x, y, size * 2.2, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      ctx.shadowBlur = 0;
      raf = requestAnimationFrame(frame);
    }

    function start() { if (!running && visible && !document.hidden) { running = true; raf = requestAnimationFrame(frame); } }
    function stop() { running = false; cancelAnimationFrame(raf); }

    layout();
    window.addEventListener('resize', layout);
    if (!img.complete) img.addEventListener('load', layout);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; visible ? start() : stop(); }).observe(wrap);
    }
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    start();
  }

  /* ---------- Art style viewer ---------- */
  var STYLES = [
    { id: 'glow', name: 'Enchanted glow', ages: '3–10', mood: 'A premium modern picture book', img: 'assets/img/style-enchanted-glow', desc: 'Our signature look. Rich painted light, golden sparkles and starry skies — pure bedtime wonder.' },
    { id: 'watercolour', name: 'Watercolour dream', ages: '0–5', mood: 'A lullaby in pictures', img: 'assets/img/style-watercolour', desc: 'Soft washes and pastel skies that melt into the page. Gentle, calm and dreamy.' },
    { id: 'fable', name: 'Classic fable', ages: '3–8', mood: 'A treasured book from Grandma's shelf', img: 'assets/img/style-classic-fable', desc: 'Fine ink lines on aged paper — the heirloom storybooks you grew up on.' },
    { id: 'anim', name: '3D animated', ages: '4–10', mood: 'Their favourite movie', img: 'assets/img/styles/3d-animated', desc: 'Cinematic, glossy and bursting with colour, like stepping into an animated film.' },
    { id: 'papercut', name: 'Paper-cut', ages: '2–8', mood: 'A handmade pop-up book', img: 'assets/img/styles/papercut', desc: 'Layered paper worlds with real shadows, like a pop-up book come alive.' },
    { id: 'clay', name: 'Clay stop-motion', ages: '2–8', mood: 'A cosy claymation', img: 'assets/img/styles/clay', desc: 'Hand-sculpted characters in a tiny handmade world. Charming and tactile.' },
    { id: 'lego', name: 'Brick world', ages: '4–12', mood: 'Everything is awesome', img: 'assets/img/styles/lego', desc: 'A blocky brick universe where your child becomes a mini-figure hero.' },
    { id: 'silhouette', name: 'Shadow play', ages: '3–8', mood: 'A magical shadow puppet show', img: 'assets/img/styles/silhouette', desc: 'Elegant silhouettes against glowing backdrops — theatrical and timeless.' }
  ];

  document.querySelectorAll('[data-style-viewer]').forEach(function (viewer) {
    var stage = viewer.querySelector('.style-stage');
    var mainImg = stage.querySelector('img');
    var soonLabel = stage.querySelector('[data-soon-file]');
    var nameEl = viewer.querySelector('[data-style-name]');
    var descEl = viewer.querySelector('[data-style-desc]');
    var agesEl = viewer.querySelector('[data-style-ages]');
    var moodEl = viewer.querySelector('[data-style-mood]');
    var tabs = viewer.querySelector('.style-tabs');

    STYLES.forEach(function (s, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'style-tab';
      b.setAttribute('aria-pressed', i === 0 ? 'true' : 'false');
      b.setAttribute('aria-controls', stage.id);
      b.dataset.id = s.id;
      var thumb = s.img
        ? '<span class="style-thumb"><picture><source srcset="' + s.img + '.webp" type="image/webp"><img src="' + s.img + '.jpg" alt="" loading="lazy" width="400" height="300"></picture></span>'
        : '<span class="style-thumb is-soon">Coming soon</span>';
      b.innerHTML = thumb + '<span>' + s.name + '</span>';
      b.addEventListener('click', function () { show(s.id); });
      tabs.appendChild(b);
      if (s.img) { var pre = new Image(); pre.src = s.img + '.jpg'; }
    });

    function show(id) {
      var s = STYLES.filter(function (x) { return x.id === id; })[0];
      tabs.querySelectorAll('.style-tab').forEach(function (t) { t.setAttribute('aria-pressed', t.dataset.id === id ? 'true' : 'false'); });
      nameEl.textContent = s.name;
      descEl.textContent = s.desc;
      if (agesEl) agesEl.textContent = s.ages;
      if (moodEl) moodEl.textContent = s.mood;
      if (!s.img) {
        stage.classList.add('is-soon');
        soonLabel.textContent = '[IMAGE: ' + s.file + '.jpg]';
        return;
      }
      stage.classList.remove('is-soon');
      mainImg.classList.add('is-leaving');
      setTimeout(function () {
        var src = mainImg.parentElement.querySelector('source');
        if (src) src.srcset = s.img + '.webp';
        mainImg.src = s.img + '.jpg';
        mainImg.alt = 'A young wizard on a hilltop above a river valley and castle, painted in the ' + s.name + ' style';
        mainImg.classList.remove('is-leaving');
      }, reduceMotion ? 0 : 280);
    }
  });

  /* ---------- Worlds filter ---------- */
  var worldFilter = document.querySelector('[data-world-filter]');
  if (worldFilter) {
    var worlds = document.querySelectorAll('.world[data-min]');
    var count = document.querySelector('[data-world-count]');
    worldFilter.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (!chip) return;
      worldFilter.querySelectorAll('.chip').forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
      var age = chip.dataset.age, shown = 0;
      worlds.forEach(function (w) {
        var ok = age === 'all' || (+w.dataset.min <= +age && +w.dataset.max >= +age);
        w.hidden = !ok;
        if (ok) shown++;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' world' : ' worlds');
    });
  }

  /* ---------- FAQ accordion + categories ---------- */
  document.querySelectorAll('.faq-list').forEach(function (list) {
    list.addEventListener('click', function (e) {
      var q = e.target.closest('.faq-q');
      if (!q) return;
      var item = q.closest('.faq-item');
      var open = !item.classList.contains('is-open');
      item.classList.toggle('is-open', open);
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  var cats = document.querySelector('[data-faq-cats]');
  if (cats) {
    cats.addEventListener('click', function (e) {
      var b = e.target.closest('.faq-cat');
      if (!b) return;
      cats.querySelectorAll('.faq-cat').forEach(function (c) { c.setAttribute('aria-pressed', c === b ? 'true' : 'false'); });
      var cat = b.dataset.cat;
      document.querySelectorAll('.faq-item[data-cat]').forEach(function (it) { it.hidden = !(cat === 'all' || it.dataset.cat === cat); });
    });
  }

  /* ---------- Chip groups in forms ---------- */
  document.querySelectorAll('[data-chip-group]').forEach(function (group) {
    var multi = group.dataset.chipGroup === 'multi';
    var hidden = group.querySelector('input[type="hidden"]');
    group.addEventListener('click', function (e) {
      var c = e.target.closest('.chip');
      if (!c) return;
      if (multi) {
        c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      } else {
        group.querySelectorAll('.chip').forEach(function (x) { x.setAttribute('aria-pressed', x === c ? 'true' : 'false'); });
      }
      if (hidden) {
        hidden.value = Array.prototype.map.call(group.querySelectorAll('.chip[aria-pressed="true"]'), function (x) { return x.dataset.value; }).join(', ');
      }
    });
  });

  /* ---------- Shortlist form ---------- */
  var form = document.querySelector('[data-shortlist]');
  if (form) {
    var success = document.querySelector('[data-shortlist-success]');
    var status = form.querySelector('.form-status');
    var submitBtn = form.querySelector('button[type="submit"]');

    function setError(input, msg) {
      var err = document.getElementById(input.id + '-error');
      input.setAttribute('aria-invalid', msg ? 'true' : 'false');
      if (err) err.textContent = msg || '';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.querySelector('#sl-email');
      var name = form.querySelector('#sl-name');
      var ok = true;
      setError(name, ''); setError(email, '');
      if (!name.value.trim()) { setError(name, 'Add your first name so we know who to write to.'); ok = false; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) { setError(email, 'Enter an email like you@example.com.'); ok = false; }
      if (!ok) { (name.value.trim() ? email : name).focus(); return; }

      var endpoint = (form.dataset.endpoint || '').trim();
      var data = new FormData(form);
      submitBtn.disabled = true;
      status.textContent = '';

      var request;
      if (!endpoint) {
        request = new Promise(function (res) { setTimeout(res, 500); }); // demo mode
      } else if (endpoint === 'netlify') {
        request = fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(data).toString() })
          .then(function (r) { if (!r.ok) throw new Error(); });
      } else {
        request = fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) { if (!r.ok) throw new Error(); });
      }

      request.then(function () {
        form.hidden = true;
        success.hidden = false;
        success.querySelector('h2').focus();
        burst(submitBtn);
      }).catch(function () {
        status.textContent = 'That didn’t send. Check your connection and try again.';
      }).finally(function () {
        submitBtn.disabled = false;
      });
    });

    var again = document.querySelector('[data-shortlist-again]');
    if (again) again.addEventListener('click', function () {
      form.reset();
      form.hidden = false;
      success.hidden = true;
      form.querySelector('#sl-hero').focus();
    });
    var copyBtn = document.querySelector('[data-copy]');
    if (copyBtn) copyBtn.addEventListener('click', function () {
      var input = document.getElementById(copyBtn.dataset.copy);
      if (navigator.clipboard) navigator.clipboard.writeText(input.value);
      else { input.select(); document.execCommand('copy'); }
      copyBtn.textContent = 'Copied';
      setTimeout(function () { copyBtn.textContent = 'Copy'; }, 1800);
    });
  }

  function burst(el) {
    if (reduceMotion || !el) return;
    var r = el.getBoundingClientRect();
    var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    for (var i = 0; i < 26; i++) {
      var d = document.createElement('span');
      d.className = 'burst';
      d.style.left = cx + 'px';
      d.style.top = cy + 'px';
      document.body.appendChild(d);
      var a = Math.random() * Math.PI * 2, dist = 60 + Math.random() * 140;
      d.animate([
        { transform: 'translate(-50%,-50%) scale(1)', opacity: 1 },
        { transform: 'translate(calc(-50% + ' + Math.cos(a) * dist + 'px), calc(-50% + ' + Math.sin(a) * dist + 'px)) scale(0)', opacity: 0 }
      ], { duration: 700 + Math.random() * 500, easing: 'cubic-bezier(.2,.8,.2,1)' }).onfinish = (function (n) { return function () { n.remove(); }; })(d);
    }
  }

  /* ---------- Login (placeholder until accounts launch) ---------- */
  var login = document.querySelector('[data-login]');
  if (login) {
    login.addEventListener('submit', function (e) {
      e.preventDefault();
      login.querySelector('.form-status').textContent = 'Accounts open at launch. Join the shortlist to get early access.';
    });
    var g = document.querySelector('[data-google]');
    if (g) g.addEventListener('click', function () {
      login.querySelector('.form-status').textContent = 'Google sign-in opens at launch. Join the shortlist to get early access.';
    });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
