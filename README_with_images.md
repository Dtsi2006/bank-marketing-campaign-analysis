
# 💼 Analyse des campagnes marketing bancaires avec Power BI

Bienvenue sur ce projet d’analyse des résultats d’une campagne marketing menée par une banque pour promouvoir un **dépôt à terme** auprès de ses clients.

## 🎯 Objectifs

- Identifier les profils types des souscripteurs (`deposit = yes`)
- Comprendre l’impact des variables marketing et relationnelles
- Optimiser les stratégies de télémarketing à partir de l’analyse des données

## 🗂️ Contenu du dépôt

```
📁 bank-marketing-campaign-analysis
├── README.md                      # Présentation du projet
├── bank.csv                       # Jeu de données brut
├── bank_data_cleaned.csv          # Jeu de données nettoyé
├── scripts/ python                # Scripts de nettoyage/analyse 
├── description dataset.txt        # Documentation des variables
└── captures/                      # Captures du dashboard
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
   - **Cibler les segments d'âge les plus prometteurs** : Prioriser les clients de 30-40 ans.
   - **Optimiser le canal de communication** : Maximiser les contacts téléphoniques.
   - **Réactiver les anciens contacts** : Relancer les clients ayant eu une expérience positive dans des campagnes précédentes.
   - **Adapter le discours en fonction du solde bancaire** : Cibler les clients avec un solde élevé.
   - **Utiliser les données sur les prêts pour personnaliser l’offre** : Adapter l'offre aux clients ayant déjà un prêt.
   - **Augmenter la fréquence des contacts pour les clients réceptifs** : Mettre en place une stratégie de relance ciblée.
   - **Analyser les tendances saisonnières** : Optimiser les moments de contact pour augmenter le taux de conversion.

## ✨ Résultats clés

- Les clients de **30-40 ans** sont les plus susceptibles de souscrire.
- Le **contact par téléphone** est plus efficace que le cellulaire ou inconnu.
- Un historique positif dans les campagnes précédentes augmente fortement la probabilité de souscription.
- Les clients avec un **solde bancaire élevé** ont un taux de souscription plus important.

## 📸 Captures d’écran

### 📸 Aperçu des graphiques

![Répartition des souscriptions selon l’âge](https://github.com/Dtsi2006/bank-marketing-campaign-analysis/raw/main/06-age_subscription.png)

![Taux de souscription par type de contact](https://github.com/Dtsi2006/bank-marketing-campaign-analysis/raw/main/07-contact_subscription.png)

### 📸 Aperçu des dashboards

![Dashboard Marketing 1](https://github.com/Dtsi2006/bank-marketing-campaign-analysis/raw/main/08-bank%20marketing%20dashboard%2001.png)

![Dashboard Marketing 2](https://github.com/Dtsi2006/bank-marketing-campaign-analysis/raw/main/09-bank%20marketing%20dashboard%2002.png)

## 📚 Ressources à consulter

- **Données** :  
  Le jeu de données est téléchargeable au lien suivant :  
  [Bank Marketing Dataset](https://www.kaggle.com/janiobachmann/bank-marketing-dataset)

## 🚀 À propos

Projet réalisé par **DJIMAFO TIOKOU , Data Analyst  

🔗 [LinkedIn](https://www.linkedin.com/in/stephane-djimafo/) | 📬 Me contacter pour échanger sur ce projet !
