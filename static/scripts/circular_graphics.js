// Récup des éléments
const ring = document.querySelector('.gauge__ring');
const valueText = document.getElementById('gauge-value');

// Fonction qui met à jour le donut
function updateGauge(pct) {
  // Sécurité : on borne entre 0 et 100
  pct = Math.max(0, Math.min(100, pct));

  // Seuils couleur: <50 vert, 50-79 jaune, >=80 rouge
  let color;
  if (pct < 50) color = '#2ecc71';          // vert
  else if (pct < 80) color = '#f1c40f';     // jaune
  else color = '#e74c3c';                   // rouge

  // Met à jour les variables CSS
  ring.style.setProperty('--p', pct);
  ring.style.setProperty('--c', color);

  // Texte central
  valueText.textContent = `${pct}%`;

  // Accessibilité (aria-label)
  ring.setAttribute('aria-label', `Progression ${pct}%`);
}

// Exemple d'utilisation : 
let valeur = 67;   // ta variable à toi
updateGauge(valeur);
