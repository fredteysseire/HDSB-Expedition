#!/usr/bin/env python3
"""Régénère les galeries de réalisations à partir de realisations.json.

Usage (depuis la racine du dépôt) : python3 outils/generer-realisations.py

Chaque page HTML peut contenir un bloc délimité par
  <!-- REALISATIONS:DEBUT limite=3 -->  ...  <!-- REALISATIONS:FIN -->
Le contenu du bloc est remplacé par les cartes des réalisations, de la plus
récente à la plus ancienne (« limite » facultative : nombre maximal de cartes).
Les cartes sont écrites en HTML statique : moteurs de recherche et assistants IA
lisent les liens sans exécuter de JavaScript.
"""
import html
import json
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parent.parent
BLOC = re.compile(r'(<!-- REALISATIONS:DEBUT(?: limite=(\d+))? -->\n)(.*?)(\s*<!-- REALISATIONS:FIN -->)', re.S)


def carte(r, indent):
    e = lambda t: html.escape(t, quote=True)
    tags = ' · '.join(e(t) for t in r.get('etiquettes', []))
    lignes = [
        '<article class="project-card">',
        f'  <a href="{e(r["page"])}">',
        '    <picture>',
        f'      <source srcset="assets/img/{e(r["image"])}.webp" type="image/webp">',
        f'      <img src="assets/img/{e(r["image"])}.jpg" alt="{e(r["alt"])}" width="{r["largeur"]}" height="{r["hauteur"]}" loading="lazy">',
        '    </picture>',
        '    <div class="project-card-body">',
        f'      <span class="project-card-tag">{tags}</span>' if tags else '',
        f'      <h3>{e(r["titre"])}</h3>',
        f'      <p>{e(r["resume"])}</p>',
        '      <span class="project-card-more">Lire l\'article →</span>',
        '    </div>',
        '  </a>',
        '</article>',
    ]
    return '\n'.join(indent + l for l in lignes if l)


def main():
    realisations = json.loads((RACINE / 'realisations.json').read_text(encoding='utf-8'))
    realisations.sort(key=lambda r: r['date'], reverse=True)
    for page in sorted(RACINE.glob('*.html')):
        texte = page.read_text(encoding='utf-8')

        def remplace(m):
            limite = int(m.group(2)) if m.group(2) else None
            debut = texte.rfind('\n', 0, m.start()) + 1
            indent = re.match(r'\s*', texte[debut:m.start()]).group(0)
            liste = realisations[:limite] if limite else realisations
            return m.group(1) + '\n'.join(carte(r, indent) for r in liste) + m.group(4)

        nouveau = BLOC.sub(remplace, texte)
        if nouveau != texte:
            page.write_text(nouveau, encoding='utf-8')
            print(f'{page.name} : galerie mise à jour')


if __name__ == '__main__':
    main()
