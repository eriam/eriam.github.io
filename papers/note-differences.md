# Note de différences : version de réflexion → version académique

## Contexte

Ce document identifie les principales différences entre la version initiale du papier de réflexion (`expert-comptable-tiers-garant.tex`) et la version académique (`expert-comptable-academique.tex`), afin de faciliter la compréhension de l'évolution du travail.

---

## 1. Structure générale

| Version réflexion | Version académique |
|---|---|
| 9 sections thématiques libres | 6 sections canoniques (intro, lit., méthode, analyse, discussion, conclusion) |
| Pas de résumé structuré | Résumé FR + EN structuré (problématique, méthode, résultats, contribution) |
| Pas de question de recherche explicite | Question de recherche formulée explicitement en introduction |
| ~8–9 pages | ~30 pages (cible SIM : max 30 p. tout compris) |
| 13 références | ~53 références dans la bibliographie académique |

---

## 2. Éléments ajoutés dans la version académique

### Revue de littérature (nouvelle section 2, ~7–8 pages)
Absente de la version initiale. Couvre cinq thématiques :
- Sociologie des professions et juridictions (Abbott 1988, Susskind & Susskind 2015, Freidson 2001)
- Profession comptable et transformation numérique (Kokina & Davenport 2017, Sutton et al. 2016, Dai & Vasarhelyi 2017)
- Gouvernance des SI dans les PME (Reix et al. 2011, Meissonier & Houzé 2010, Cragg & King 1993, Thong 1999)
- Code normatif et responsabilité du logiciel (Lessig 1999/2006, Zittrain 2008, Féral-Schuhl 2022, directive 2024/2853)
- Théorie économique des tiers de confiance (Akerlof 1970, Williamson 1985, North 1990)

### Cadre théorique et méthodologie (nouvelle section 3, ~4 pages)
Absente de la version initiale. Explicite les quatre cadres mobilisés et qualifie méthodologiquement la contribution comme "essai théorique argumenté à vocation prospective" (Weick 1989, Whetten 1989 ; Ansoff 1975, Godet 2007).

### Section Discussion (nouvelle section 5, ~5 pages)
Absente de la version initiale. Couvre : limites de l'analyse, hypothèses alternatives (grands réseaux, solution réglementaire de marché, inertie professionnelle), implications théoriques pour trois champs, trois axes de recherche empirique.

### Tableau comparatif des acteurs (Tableau 1)
Formalisation en tableau de l'analyse comparative des acteurs candidats à la fonction de tiers garant.

### Déclaration IA
Ajoutée dans la page de garde conformément aux exigences de SIM.

---

## 3. Éléments transformés

### Dimension machiavélienne (section 7 de la version réflexion)
**Avant :** Section structurante de 4 sous-sections sur la *virtù* et la *fortuna*, mobilisant explicitement Machiavel comme cadre central.  
**Après :** Réduit à quelques lignes dans la section Discussion (hypothèse de l'asymétrie d'information comme fenêtre stratégique), présenté comme une lecture possible, sans en faire un axe structurant. Le ton prescriptif ("la lucidité stratégique est un acte responsable") est éliminé.  
**Pourquoi :** Trop normatif et trop polémique pour une revue académique en double aveugle. La référence à Machiavel peut être perçue comme manquant de distance critique.

### Ton général
**Avant :** Ton de conviction, parfois prescriptif ("la profession doit", "la fenêtre se refermera"). Formulations directes à la deuxième personne du pluriel implicite.  
**Après :** Ton académique strict, troisième personne, formulations conditionnelles ("il apparaît que", "il est possible d'envisager", "cette analyse conduit à formuler l'hypothèse"). Toute affirmation factuelle non triviale est sourcée.

### Calcul économique (ancienne section 7)
**Avant :** Présenté comme une analyse opérationnelle.  
**Après :** Explicitement présenté comme "hypothèses de travail, non comme des prévisions", avec mention des hypothèses sous-jacentes et des conditions de réalisation.

### Données cyber
**Avant :** Présentées comme certitudes.  
**Après :** Sourcées systématiquement (CNIL 2024, ANSSI 2025, CESIN 2025, Hiscox 2024) avec mention de leur nature d'indicateurs, non d'estimations exhaustives.

---

## 4. Éléments supprimés dans la version académique

| Élément supprimé | Justification |
|---|---|
| Analyse sectorielle spécifique de certains acteurs nommés | Trop opérationnel, risque de perception partisane |
| Scénarios FUD (fear, uncertainty, doubt) | Non adaptés à une revue académique |
| Appel à l'action direct ("les cabinets qui attendent...") | Ton entrepreneurial incompatible avec le registre académique |
| Section "Hypothèse de la vigilance collective" (section 10) | Trop spéculative pour constituer une section de développement ; peut être mentionnée en discussion ou dans un article séparé |

---

## 5. Bibliographie

| Version réflexion | Version académique |
|---|---|
| 13 entrées (biblatex authoryear) | 53 entrées (biblatex authoryear, compatible APA) |
| Entrées principalement textes législatifs et rapports | Ajout de : Abbott, Susskind, Freidson, Dubar/Tripier, Kokina/Davenport, Sutton et al., Dai/Vasarhelyi, Reix et al., Orlikowski, Meissonier/Houzé, Venkatesh et al., Cragg/King, Thong, Zittrain, Féral-Schuhl, Williamson, Akerlof, North, DiMaggio/Powell, Scott, LeCun/Bengio/Hinton, Brynjolfsson/McAfee, Frey/Osborne, Topol, Eastman et al., Weick, Whetten, Ansoff, Godet, directive 2024/2853 |

**Entrées à vérifier avant soumission :**
- Numéros de page exacts pour les articles de revue (Kokina 2017, Sutton 2016, Meissonier 2010, etc.)
- Numéro exact de l'édition de Féral-Schuhl Cyberdroit (indiqué 9e éd. 2022)
- Journal officiel exact pour la directive 2024/2853 (numéro L non encore précisé)
- Vérifier si `frey2013` est bien une publication Oxford Martin School ou un article de revue

---

## 6. Compatibilité avec les deux revues

| Critère | SIM | RFG | Version académique |
|---|---|---|---|
| Langue | FR ou EN | FR | FR ✓ |
| Max pages | 30 (template SIM) | ~25–35 (estimé) | ~30 ✓ |
| Résumé bilingue | FR + EN requis | FR + EN recommandé | ✓ |
| Question de recherche explicite | Requis | Recommandé | ✓ |
| Revue de littérature | Requis | Requis | ✓ |
| Format fichier | Word/ODT (SIM) | À vérifier | Conversion LaTeX → DOCX nécessaire pour SIM |
| Bibliographie .bib | Requis (SIM) | À vérifier | Fichier .bib fourni ✓ |

**Pour SIM :** La soumission requiert un fichier Word/ODT, non LaTeX. Conversion nécessaire (Pandoc ou via LaTeX → PDF → reformatage). SIM impose l'utilisation de son template stylesheet — vérifier sur revuesim.org.

**Pour RFG :** Vérifier les guidelines sur rfg.revuesonline.com (JLE).
