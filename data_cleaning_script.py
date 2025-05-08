
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv('bank.csv')

# Afficher les premières lignes
print(df.head())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Nettoyage basique
df_cleaned = df.copy()
df_cleaned['job'] = df_cleaned['job'].replace('unknown', pd.NA)
df_cleaned['education'] = df_cleaned['education'].replace('unknown', pd.NA)
df_cleaned['contact'] = df_cleaned['contact'].replace('unknown', pd.NA)
df_cleaned['poutcome'] = df_cleaned['poutcome'].replace('unknown', pd.NA)

# Sauvegarder les données nettoyées
df_cleaned.to_csv('bank_data_cleaned.csv', index=False)

# Statistiques descriptives
print(df_cleaned.describe())

# Visualisation : souscription selon l’âge
plt.figure(figsize=(10,6))
sns.histplot(data=df_cleaned, x='age', hue='deposit', multiple='stack', bins=30)
plt.title('Répartition des souscriptions selon l’âge')
plt.xlabel('Âge')
plt.ylabel('Nombre de clients')
plt.show()

# Taux de souscription par type de contact
contact_subscription = pd.crosstab(df_cleaned['contact'], df_cleaned['deposit'], normalize='index') * 100
print(contact_subscription)

# Graphique du taux de souscription par contact
contact_subscription['yes'].plot(kind='bar', color='skyblue')
plt.title('Taux de souscription par type de contact (%)')
plt.ylabel('Pourcentage de souscription')
plt.show()
