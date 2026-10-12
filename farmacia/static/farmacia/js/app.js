// Efectos tipo React Bits en JavaScript puro
(function () {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // SplitText: anima cada letra del texto
  document.querySelectorAll('[data-split]').forEach((el) => {
    const text = el.textContent.trim();
    el.textContent = '';
    el.setAttribute('aria-label', text);
    el.classList.add('split');
    [...text].forEach((ch, i) => {
      const span = document.createElement('span');
      span.className = 'char' + (ch === ' ' ? ' space' : '');
      span.textContent = ch === ' ' ? ' ' : ch;
      span.style.setProperty('--i', i);
      span.setAttribute('aria-hidden', 'true');
      el.appendChild(span);
    });
  });

  // SpotlightCard: el brillo sigue al ratón
  document.querySelectorAll('.spotlight').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      card.style.setProperty('--mx', `${e.clientX - r.left}px`);
      card.style.setProperty('--my', `${e.clientY - r.top}px`);
    });
  });

  // CountUp: los números suben desde 0
  const countUp = (el) => {
    const target = parseFloat(el.dataset.count);
    const decimals = parseInt(el.dataset.decimals || '0', 10);
    const prefix = el.dataset.prefix || '';
    const fmt = (v) => prefix + v.toLocaleString('es', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals,
    });
    if (reduceMotion || !target) { el.textContent = fmt(target || 0); return; }
    const duration = 1400;
    const start = performance.now();
    const tick = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 4);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  // AnimatedContent: aparece al entrar en pantalla
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in');
        entry.target.querySelectorAll('[data-count]').forEach(countUp);
        io.unobserve(entry.target);
      });
    }, { threshold: 0.12 });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('in'));
    document.querySelectorAll('[data-count]').forEach(countUp);
  }

  // Búsqueda y filtros del catálogo
  const search = document.getElementById('search');
  const chips = document.querySelectorAll('.chip');
  const products = document.querySelectorAll('.product[data-name]');
  const noResults = document.querySelector('.no-results');
  let filter = 'all';

  const applyFilters = () => {
    const q = (search ? search.value : '').trim().toLowerCase();
    let visible = 0;
    products.forEach((p) => {
      const match = p.dataset.name.includes(q) && (filter === 'all' || p.dataset.status === filter);
      p.hidden = !match;
      if (match) visible++;
    });
    if (noResults) noResults.classList.toggle('show', products.length > 0 && visible === 0);
  };

  if (search) search.addEventListener('input', applyFilters);
  chips.forEach((chip) => chip.addEventListener('click', () => {
    chips.forEach((c) => c.classList.remove('active'));
    chip.classList.add('active');
    filter = chip.dataset.filter;
    applyFilters();
  }));

  // Atajo: "/" enfoca la búsqueda
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && search && document.activeElement !== search) {
      e.preventDefault();
      search.focus();
    }
  });

  // Toasts: se cierran solos
  document.querySelectorAll('.toast').forEach((toast) => {
    const close = () => {
      toast.classList.add('hide');
      setTimeout(() => toast.remove(), 400);
    };
    toast.querySelector('.toast-close')?.addEventListener('click', close);
    setTimeout(close, 4500);
  });
})();
