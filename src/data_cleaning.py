import pandas as pd

def load_data(file_path):
    """Charge les données depuis un fichier CSV."""
    return pd.read_csv(file_path, sep=";", encoding="utf-8")

def clean_data(df):
    """Nettoie les données en supprimant les lignes avec des valeurs manquantes."""
    print("Valeurs manquantes :\n", df.isnull().sum())
    df = df.dropna()
    return df

def display_statistics(df):
    """Affiche les statistiques descriptives des données pour les années 2021 et 2022."""
    stats_columns = ['écrans', 'fauteuils', 'entrées 2021', 'entrées 2022']
    for col in stats_columns:
        if col not in df.columns:
            raise KeyError(f"La colonne {col} est absente du DataFrame.")
    print("Les statistiques descriptives :\n", df[stats_columns].describe())
