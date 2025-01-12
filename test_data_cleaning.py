from src.data_cleaning import load_data, clean_data, display_statistics

file_path = "data/cinemas.csv"

df = load_data(file_path)

print("Aperçu des données :\n", df.head())

df_clean = clean_data(df)

print("Données nettoyées :\n", df_clean.head())

display_statistics(df_clean)
