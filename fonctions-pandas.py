import pandas as pd
import numpy as np

# Données initiales
data = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
    'B': ['one', 'one', 'two', 'two', 'one', 'two'],
    'C': [1, 2, 3, 4, 5, 6],
    'D': [7, 8, 9, 10, 11, 12],
    'E': [10, 20, 30, 40, 50, 60]
})

# 1. ARGpartition - Obtenir les indices des k plus petites valeurs
print("1. ARGpartition() Example:")
print(np.argpartition(data['C'], 2))  # Indices des 2 plus petits éléments
print()

# 2. ALLCLOSE - Vérifier si deux tableaux sont proches
print("2. ALLCLOSE() Example:")
arr1 = np.array([1.0, 2.001, 3.0001])
arr2 = np.array([1.0, 2.0, 3.0])
print(np.allclose(arr1, arr2, atol=0.01))  # Résultat: True
print()

# 3. CLIP - Limiter les valeurs entre min et max
print("3. CLIP() Example:")
print(data['C'].clip(lower=2, upper=4))  # Limite les valeurs entre 2 et 4
print()

# 4. EXTRACT - Extraire des données avec regex
print("4. EXTRACT() Example:")
names = pd.Series(['John Doe', 'Jane Smith'])
print(names.str.extract(r'(\w+)\s+(\w+)'))  # Extrait prénom et nom
print()

# 5. WHERE - Applique une condition
print("5. WHERE() Example:")
print(data['C'].where(data['C'] > 2, np.nan))  # Remplace valeurs <= 2 par NaN
print()

# 6. PERCENTILE - Calculer un percentile
print("6. PERCENTILE() Example:")
print(np.percentile(data['C'], 50))  # 50e percentile (médiane)
print()

# 7. READ_CSV (NROWS) - Lire N premières lignes
print("7. READ_CSV(NROWS=N) Example:")
# Exemple local (lecture d'un fichier réel non nécessaire ici)
sample_data = pd.read_csv(pd.compat.StringIO("A,B,C\n1,2,3\n4,5,6"), nrows=1)
print(sample_data)
print()

# 8. MAP - Appliquer un mapping
print("8. MAP() Example:")
mapping = {1: 'one', 2: 'two', 3: 'three'}
print(data['C'].map(mapping))  # Remplace valeurs 1, 2, 3 par noms
print()

# 9. APPLY - Appliquer une fonction
print("9. APPLY() Example:")
print(data['C'].apply(lambda x: x**2))  # Élève chaque élément au carré
print()

# 10. ISIN - Vérifier si les éléments sont dans une liste
print("10. ISIN() Example:")
print(data['A'].isin(['foo']))  # Vérifie si 'A' contient 'foo'
print()

# 11. COPY - Créer une copie
print("11. COPY() Example:")
data_copy = data.copy()  # Crée une copie
data_copy['C'] = 0  # Modifie la copie
print(data)
print(data_copy)
print()

# 12. SELECT_DTYPES - Sélectionner les colonnes par type
print("12. SELECT_DTYPES() Example:")
print(data.select_dtypes(include='int64'))  # Colonnes entières
print()

# 13. PIVOT_TABLE - Créer un tableau croisé dynamique
print("13. PIVOT_TABLE() Example:")
pivot = data.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
print(pivot)
print()

# 14. DESCRIBE - Statistiques descriptives
print("14. DESCRIBE() Example:")
print(data.describe())  # Moyenne, min, max, etc.
print()

# 15. DROPNA - Supprimer les valeurs manquantes
print("15. DROPNA() Example:")
data_with_nan = data.copy()
data_with_nan.loc[0, 'C'] = np.nan  # Ajoute NaN
print(data_with_nan.dropna())  # Supprime les lignes contenant NaN
print()

# 16. FILLNA - Remplir les NaN
print("16. FILLNA() Example:")
print(data_with_nan.fillna(0))  # Remplace NaN par 0
print()

# 17. MERGE - Fusionner deux DataFrames
print("17. MERGE() Example:")
data1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
data2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})
merged = pd.merge(data1, data2, on='key', how='inner')  # Fusion sur clé
print(merged)
print()

# 18. GROUPBY - Grouper les données
print("18. GROUPBY() Example:")
grouped = data.groupby('A')['C'].sum()  # Somme groupée par 'A'
print(grouped)
print()

# 19. SORT_VALUES - Trier les données
print("19. SORT_VALUES() Example:")
print(data.sort_values(by='C', ascending=False))  # Trie par 'C' (desc)
print()

# 20. VALUE_COUNTS - Compter les occurrences
print("20. VALUE_COUNTS() Example:")
print(data['A'].value_counts())  # Compte les valeurs uniques dans 'A'
print()

# 21. DROP_DUPLICATES - Supprimer les doublons
print("21. DROP_DUPLICATES() Example:")
data_with_dup = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo'],
    'B': [1, 2, 1, 2, 1]
})
print(data_with_dup.drop_duplicates())  # Supprime les doublons
print()

# 22. CUMSUM - Calculer la somme cumulative
print("22. CUMSUM() Example:")
print(data['C'].cumsum())  # Somme cumulative des éléments de 'C'
print()

# 23. SHIFT - Décaler les données
print("23. SHIFT() Example:")
print(data['C'].shift(1))  # Décale les valeurs de 'C' d'une ligne vers le bas
print()

# 24. ROLLING - Calculer une fenêtre glissante
print("24. ROLLING() Example:")
print(data['C'].rolling(window=2).mean())  # Moyenne mobile sur une fenêtre de 2
print()

# 25. EXPLODE - Séparer les éléments d'une liste dans une colonne
print("25. EXPLODE() Example:")
df_explode = pd.DataFrame({'A': [1, 2], 'B': [[1, 2], [3, 4]]})
print(df_explode.explode('B'))  # Sépare les listes dans la colonne 'B'
print()

# 26. CONCAT - Concatenation de DataFrames
print("26. CONCAT() Example:")
df1 = pd.DataFrame({'A': ['foo', 'bar'], 'B': [1, 2]})
df2 = pd.DataFrame({'A': ['baz', 'qux'], 'B': [3, 4]})
concat_df = pd.concat([df1, df2], axis=0)  # Concatenation verticale
print(concat_df)
print()

# 27. CUT - Binning de valeurs en intervalles
print("27. CUT() Example:")
print(pd.cut(data['E'], bins=3, labels=['Low', 'Medium', 'High']))  # Classe les valeurs en 3 intervalles
print()

# 28. QUERY - Filtrer les données par une condition
print("28. QUERY() Example:")
print(data.query('C > 3'))  # Sélectionne les lignes où 'C' > 3
print()
