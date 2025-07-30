import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("C:\\Users\\inesd\\OneDrive\\Bureau\\student-life-database-main\\student_depression_dataset_clean.csv", sep=';')

# Nettoyer les noms de colonnes
colonnes_nettoyees = []  # Une nouvelle liste vide

for i in df.columns:  # Pour chaque nom de colonne existant
    colonnes_nettoyees.append(i.strip())  # On enlève les espaces et on ajoute à la liste

# On remplace les anciennes colonnes par les nouvelles colonnes propres
df.columns = colonnes_nettoyees

# === Étape 2 : Créer la table city ===
city_df = df[['City']].drop_duplicates().reset_index(drop=True)
city_df['id'] = city_df.index + 1  # créer une colonne ID
city_df.rename(columns={'City': 'name'}, inplace=True)
city_df = city_df[['id', 'name']]


# === Étape 3 : Créer la table profession ===
profession_df = df[['Profession']].drop_duplicates().reset_index(drop=True)
profession_df['id'] = profession_df.index + 1  # créer une colonne ID
profession_df.rename(columns={'Profession': 'name'}, inplace=True)
profession_df = profession_df[['id', 'name']] # Reordonner les colonnes : d'abord id, puis name


#les merges avec les id city et profession pour la table perosn
df = df.merge(city_df[['id', 'name']], left_on='City', right_on='name')
df.rename(columns={'id_y': 'city_id'}, inplace=True)

df = df.merge(profession_df[['id', 'name']], left_on='Profession', right_on='name')
df.rename(columns={'id': 'profession_id'}, inplace=True)


# === Étape 4 : Créer la table person ===
person_df = df[['Gender', 'Age', 'Degree', 'city_id', 'profession_id']].reset_index(drop=True)
person_df['id'] = person_df.index + 1
person_df = person_df[['id', 'Gender', 'Age', 'Degree', 'city_id', 'profession_id']]
df.drop(columns=['name_x', 'name_y', 'id_x'], inplace=True)
person_df.rename(columns={
    "Gender": "gender",
    "Age": "age",
    "Degree": "degree"
}, inplace=True)

#les merges avec l'id person pour la table mental health
df['person_id'] = person_df['id']


# === Étape 5 : Créer la table mental health ===
mentalhealth_df = df[['person_id', 'Depression', 'Have you ever had suicidal thoughts ?', 'Sleep Duration', 'Family History of Mental Illness', 'Financial Stress', 'Dietary Habits']].reset_index(drop=True)
mentalhealth_df = mentalhealth_df[['person_id', 'Depression' ,'Have you ever had suicidal thoughts ?', 'Sleep Duration', 'Family History of Mental Illness', 'Financial Stress', 'Dietary Habits']]
mentalhealth_df.rename(columns={
    'Have you ever had suicidal thoughts ?': 'suicidal_thoughts',
    'Sleep Duration': 'sleep_duration',
    'Family History of Mental Illness': 'family_history',
    'Financial Stress': 'financial_stress',
    'Dietary Habits': 'dietary_habits',
    'Depression': 'depression'
}, inplace=True)

# === Étape 6 : Créer la table academic work ===
academicwork_df = df[['person_id', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction', 'Work/Study Hours']].reset_index(drop=True)
academicwork_df = academicwork_df[['person_id', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction', 'Job Satisfaction', 'Work/Study Hours']]
academicwork_df.rename(columns={
    'Academic Pressure': 'academic_pressure',
    'Work Pressure': 'work_pressure',
    'CGPA': 'cgpa',
    'Study Satisfaction': 'study_satisfaction',
    'Job Satisfaction': 'job_satisfaction',
    'Work/Study Hours': 'work_study_hours'
}, inplace=True) 


# Pour mental_health
bool_map = {'VRAI': True, 'FAUX': False}
mentalhealth_df['depression'] = mentalhealth_df['depression'].map(bool_map)
mentalhealth_df['suicidal_thoughts'] = mentalhealth_df['suicidal_thoughts'].map(bool_map)
mentalhealth_df['family_history'] = mentalhealth_df['family_history'].map(bool_map)
# Pour academic_work
academicwork_df['cgpa'] = academicwork_df['cgpa'].str.replace(',', '.').astype(float)


#Sauvegarder chaque table
person_df = person_df.drop(columns=["id"], errors="ignore")
person_df.to_csv("person.csv", index=False)

city_df = city_df.drop(columns=["id"], errors="ignore")
city_df.to_csv("city.csv", index=False)

profession_df = profession_df.drop(columns=["id"], errors="ignore")
profession_df.to_csv("profession.csv", index=False)

mentalhealth_df.to_csv("mental_health.csv", index=False)
academicwork_df.to_csv("academic_work.csv", index=False)



