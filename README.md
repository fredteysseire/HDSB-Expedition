# HDSB Expédition, site internet

Site vitrine de HDSB (nom commercial HDSB-XP / HDSB Expédition), préparation et aménagement de
véhicules d'expédition poids lourds à Sernhac (Gard), publié sur **https://hdsb-xp.com**.
Site statique HTML/CSS + un script PHP pour le formulaire, prévu pour un hébergement mutualisé
Apache/PHP. Aucun cookie, aucun traceur, aucune police externe.

## Pages

| Fichier | Rôle |
|---|---|
| `index.html` | Présentation : société, savoir-faire, plateformes, fondateurs, méthode |
| `contact.html` | Formulaire de contact (envoi via `api/contact.php`) |
| `merci.html` | Confirmation d'envoi (non indexée) |
| `mentions-legales.html` | Mentions légales, RGPD, cookies |

## Avant la mise en ligne (à faire)

- [ ] **Email du formulaire** : `api/contact.php` envoie à `contact@hdsb-xp.com` depuis cette même
      adresse (constantes `DESTINATAIRE` / `EXPEDITEUR`). La boîte doit exister chez l'hébergeur.
- [ ] **Domaines** : `hdsb-xp.com` est le domaine principal (site OVH « Website-www », dossier `www`).
      `hdsb-xp.fr` est un site OVH séparé (dossier `aaol5xz76e`) : y déposer **uniquement**
      `redirection-fr/.htaccess`, qui renvoie tout le .fr en 301 vers `https://hdsb-xp.com`.
      Ajouter aussi `www.hdsb-xp.fr` à ce site .fr.
- [ ] **SSL** : activer le certificat pour les quatre noms ci-dessus avant de déposer le `.htaccess`
      (il force https ; sans certificat, la redirection affiche une alerte de sécurité).
- [ ] **Test réel** : envoyer un message depuis le site en ligne et vérifier sa réception (et le dossier spam).
- [ ] **Photos réelles** (atelier, camions en cours, détails) : à ajouter dès que disponibles.
- [ ] Après la mise en ligne : déclarer le site dans Google Search Console et créer la fiche Google Business Profile.

## Mettre à jour les actualités (`actualites.html`)

- **Ajouter un salon** : copier un bloc `<li class="event" data-end="AAAA-MM-JJ">` dans
  `<ul id="agenda-avenir">` et adapter dates, nom, lieu. `data-end` = dernier jour du salon :
  le lendemain, le salon passe tout seul dans « Salons passés ».
- **Ajouter une information** : copier un bloc `<article class="news-item">` en haut de
  `<div class="news-list">` (la plus récente en premier).
- **Encart de l'accueil** : le bandeau du salon (`<aside class="news-strip" data-until="2026-11-15">`)
  s'affiche jusqu'au 15 novembre 2026 inclus puis se masque. Pour le salon suivant, changer le
  texte et la date `data-until`.

## Déploiement

Mise en ligne automatique par l'intégration Git d'OVH : la branche `main` de ce dépôt est publiée
dans le dossier `www` de l'hébergement (site OVH « Website-www »). Toute modification fusionnée dans
`main` part en ligne. `README.md`, `.git*` et `redirection-fr/` sont publiés avec le dépôt mais
renvoient une 404 (règle du `.htaccess`). Le `.htaccess` du dossier du .fr se dépose à part, par FTP.
Le dossier `api/data/` doit être accessible en écriture par PHP ; il est protégé de l'accès public
par son `.htaccess` et contient, si besoin, les demandes dont l'email n'a pas pu partir
(`messages-non-envoyes.txt`) et les envois écartés comme robots (`messages-suspects.txt`).

## Visuels

- Logo et fond d'accueil issus de la charte graphique HDSB (`assets/img/`).
- Police Montserrat (SIL Open Font License, voir `assets/fonts/OFL.txt`), hébergée localement.
