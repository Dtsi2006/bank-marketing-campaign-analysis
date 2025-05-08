
# 💼 Analyse des campagnes marketing bancaires avec Power BI

Bienvenue sur ce projet d’analyse des résultats d’une campagne marketing menée par une banque pour promouvoir un **dépôt à terme** auprès de ses clients.

## 🎯 Objectifs

- Identifier les profils types des souscripteurs (`deposit = yes`)
- Comprendre l’impact des variables marketing et relationnelles
- Optimiser les stratégies de télémarketing à partir de l’analyse des données

## 🗂️ Contenu du dépôt

```
📁 bank-marketing-campaign-analysis
├── bank.csv                       # Jeu de données brut
├── bank_data_cleaned.csv          # Jeu de données nettoyé
├── BANK MARKETING DASHBOARD.pbix  # Fichier Power BI
├── DESCRIPTION DU DATA SET.txt    # Documentation des variables
├── README.md                      # Présentation du projet
├── captures/                      # Captures du dashboard (à ajouter)
└── scripts/                       # Scripts de nettoyage/analyse (si Python ajouté)
```

## 📊 Aperçu des données

- 11 162 clients
- 17 variables : âge, profession, statut marital, éducation, prêts, type de contact, résultats des campagnes précédentes...
- Variable cible : **le client a-t-il souscrit au dépôt à terme ?**

## 🛠️ Logiciels et outils utilisés

- **Power BI Desktop** → Analyse visuelle et création du dashboard
- **Python (pandas, matplotlib) / Excel** → Nettoyage et exploration initiale des données
- **GitHub** → Partage et versioning du projet

## 🏛️ Architecture du projet

1. **Préparation des données**
   - Nettoyage (`bank.csv` → `bank_data_cleaned.csv`)
   - Gestion des valeurs manquantes, normalisation des catégories

2. **Analyse exploratoire**
   - Statistiques descriptives : moyenne d’âge, distribution des statuts
   - Visualisation : répartition des souscripteurs selon les variables clés

3. **Dashboard Power BI**
   - Vue globale : taux de souscription
   - Profils clients : âge, solde, profession
   - Analyse des campagnes : type et durée des contacts, résultats précédents

4. **Recommandations stratégiques**
   - Suggestions pour améliorer l’efficacité du télémarketing

## ✨ Résultats clés

- Les clients de **30-40 ans** sont les plus susceptibles de souscrire.
- Le **contact par téléphone** est plus efficace que le cellulaire ou inconnu.
- Un historique positif dans les campagnes précédentes augmente fortement la probabilité de souscription.
- Les clients avec un **solde bancaire élevé** ont un taux de souscription plus important.

## 📸 Captures d’écran

*À ajouter :*
```
captures/dashboard_apercu.png
captures/age_subscription.png
captures/contact_subscription.png
```

## 🚀 À propos

Projet réalisé par **DJIMAFO TIOKOU STEPHANE** — 2025

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/) *(remplace par ton lien LinkedIn)*
