// Comportements du site HDSB Expédition (aucune dépendance, aucun traceur).
(function () {
  // Menu mobile
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('nav-links');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', (e) => {
      if (e.target.closest('a')) {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Encarts d'actualité datés (ex. salon) : visibles jusqu'à la fin du jour data-until inclus,
  // puis masqués sans intervention.
  const today = new Date();
  document.querySelectorAll('[data-until]').forEach((el) => {
    const end = new Date(el.getAttribute('data-until') + 'T23:59:59');
    if (!isNaN(end) && today <= end) {
      el.hidden = false;
    }
  });

  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = today.getFullYear();
  });

  // Formulaire de contact (envoi par api/contact.php) : affiche l'erreur au retour d'un envoi
  // échoué (contact.html?envoi=erreur) et bloque le double clic pendant l'envoi.
  const form = document.getElementById('contact-form');
  if (form) {
    const formError = document.getElementById('form-error');
    if (formError && new URLSearchParams(window.location.search).get('envoi') === 'erreur') {
      formError.hidden = false;
    }
    const submitBtn = form.querySelector('button[type="submit"]');
    // Anti-robots : temps passé sur la page, vérifié par api/contact.php (les robots postent
    // directement sur le script sans afficher la page).
    const shownAt = Date.now();
    form.addEventListener('submit', () => {
      let verif = form.querySelector('input[name="verif"]');
      if (!verif) {
        verif = document.createElement('input');
        verif.type = 'hidden';
        verif.name = 'verif';
        form.appendChild(verif);
      }
      verif.value = String(Date.now() - shownAt);
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = 'Envoi en cours…';
      }
    });
    // Retour arrière vers une page restée en cache : réactive le bouton.
    window.addEventListener('pageshow', (e) => {
      if (e.persisted && submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Envoyer ma demande';
      }
    });
  }
})();
