// ⚙ URL de votre Firebase Realtime Database
const DB = 'https://francis-valoren-default-rtdb.europe-west1.firebasedatabase.app';

function flagEmoji(code) {
    if (!code || code.length !== 2) return '🌍';
    return [...code.toUpperCase()].map(c =>
        String.fromCodePoint(c.charCodeAt(0) + 127397)
    ).join('');
}

async function initTracker() {
    const countEl = document.getElementById('visiteCount');
    const paysEl  = document.getElementById('visitePays');

    try {
        // Détection du pays du visiteur
        let pays = 'XX';
        try {
            const geo = await fetch('https://ipapi.co/json/');
            const geoData = await geo.json();
            pays = geoData.country_code || 'XX';
        } catch (_) {}

        // Enregistrement de la visite
        await fetch(`${DB}/visites.json`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ t: Date.now() })
        });

        // Enregistrement du pays (clé = déduplication automatique)
        await fetch(`${DB}/pays/${pays}.json`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: 'true'
        });

        // Comptage des visites (shallow = clés seulement, léger)
        const r1 = await fetch(`${DB}/visites.json?shallow=true`);
        const d1 = await r1.json();
        const total = d1 ? Object.keys(d1).length : 0;

        // Récupération des pays uniques
        const r2 = await fetch(`${DB}/pays.json`);
        const d2 = await r2.json();
        const drapeaux = d2 ? Object.keys(d2).map(flagEmoji).join(' ') : '';

        if (countEl) countEl.textContent = total.toLocaleString('fr-FR') + ' visites';
        if (paysEl)  paysEl.textContent  = drapeaux;

    } catch (_) {
        if (countEl) countEl.textContent = '— visites';
    }
}

document.addEventListener('DOMContentLoaded', initTracker);
