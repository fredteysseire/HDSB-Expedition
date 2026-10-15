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
- [ ] **Domaines** : `hdsb-xp.com` est le domaine principal. Rattacher aussi `www.hdsb-xp.com`,
      `hdsb-xp.fr` et `www.hdsb-xp.fr` au même hébergement (multisite OVH) : le `.htaccess` les
      redirige tous en 301 vers `https://hdsb-xp.com`.
- [ ] **SSL** : activer le certificat pour les quatre noms ci-dessus avant de déposer le `.htaccess`
      (il force https ; sans certificat, la redirection affiche une alerte de sécurité).
- [ ] **Test réel** : envoyer un message depuis le site en ligne et vérifier sa réception (et le dossier spam).
- [ ] **Photos réelles** (atelier, camions en cours, détails) : à ajouter dès que disponibles.
- [ ] Après la mise en ligne : déclarer le site dans Google Search Console et créer la fiche Google Business Profile.

## Encart « Salon »

L'encart Vanlife Expo Bordeaux de l'accueil (`<aside class="news-strip" data-until="2026-11-15">`)
s'affiche jusqu'au 15 novembre 2026 inclus puis se masque automatiquement. Pour un prochain salon,
modifier le texte et la date `data-until`.

## Déploiement

Copier tout le contenu du dépôt à la racine web de l'hébergement (FTP/SFTP), sauf `README.md` et `.git`.
Le dossier `api/data/` doit être accessible en écriture par PHP ; il est protégé de l'accès public
par son `.htaccess` et contient, si besoin, les demandes dont l'email n'a pas pu partir
(`messages-non-envoyes.txt`) et les envois écartés comme robots (`messages-suspects.txt`).

## Visuels

- Logo et fond d'accueil issus de la charte graphique HDSB (`assets/img/`).
- Police Montserrat (SIL Open Font License, voir `assets/fonts/OFL.txt`), hébergée localement.
