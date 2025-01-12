import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(df):
    """Prépare les données pour l'entraînement et le test."""
    required_columns = ['écrans', 'fauteuils', 'population de la commune', 'entrées 2022']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"La colonne {col} est absente du DataFrame.")

    X = df[['écrans', 'fauteuils', 'population de la commune']]
    y = df['entrées 2022']
    return train_test_split(X, y, test_size=0.2, random_state=42)
