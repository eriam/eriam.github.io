# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

GitHub Pages personal site at `eriam.github.io`. Plain HTML, no CSS, no JS, no framework — intentional aesthetic choice.

## Structure

- `index.html` — landing page (French): axes de travail, activités, publications, projets, contact.
- `dashboard-bts/dashboard_bts_sio.html` — dashboard d'analyse BTS (effectifs, cartographie, insertion professionnelle) via Leaflet et données data.gouv.fr / InserJeunes DEPP. Données dans `dashboard-bts/pipeline/output/`.
- `cv.pdf` — CV local, non lié depuis le site.

## Deployment

GitHub Pages sert la branche `main` à la racine. Pas de build step — les fichiers sont servis tels quels.
