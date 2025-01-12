import matplotlib.pyplot as plt
import seaborn as sns

def calculate_mean_entries(df):
    """Calcule les entrées moyennes par fauteuil pour chaque région."""
    required_columns = ['région administrative', 'entrées 2021', 'entrées 2022', 'fauteuils']
    for col in required_columns:
        if col not in df.columns:
            raise KeyError(f"La colonne {col} est absente du DataFrame.")

    df = df.copy()
    df['entrees_2021_par_fauteuil'] = df['entrées 2021'] / df['fauteuils']
    df['entrees_2022_par_fauteuil'] = df['entrées 2022'] / df['fauteuils']

    moyennes_par_region_2021 = df.groupby('région administrative')['entrees_2021_par_fauteuil'].mean()
    moyennes_par_region_2022 = df.groupby('région administrative')['entrees_2022_par_fauteuil'].mean()

    return moyennes_par_region_2021, moyennes_par_region_2022

def plot_top_regions(moyennes_par_region_2021, moyennes_par_region_2022):
    """Affiche les 10 régions avec les meilleures entrées moyennes par fauteuil pour 2021 et 2022."""
    top_10_regions_2021 = moyennes_par_region_2021.sort_values(ascending=False).head(10)
    top_10_regions_2022 = moyennes_par_region_2022.sort_values(ascending=False).head(10)

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    top_10_regions_2021.plot(kind='bar', color='skyblue', ax=axes[0])
    axes[0].set_title("Entrées moyennes par fauteuil pour les 10 premières régions (2021)")
    axes[0].set_ylabel("Entrées moyennes par fauteuil")
    axes[0].set_xlabel("Régions")
    axes[0].tick_params(axis='x', rotation=45)

    top_10_regions_2022.plot(kind='bar', color='lightcoral', ax=axes[1])
    axes[1].set_title("Entrées moyennes par fauteuil pour les 10 premières régions (2022)")
    axes[1].set_ylabel("Entrées moyennes par fauteuil")
    axes[1].set_xlabel("Régions")
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def get_top_and_bottom_regions(moyennes_par_region, n=3):
    """
    Identifie les régions avec les meilleures et les pires moyennes par fauteuil.
    :param moyennes_par_region: Série contenant les moyennes par région.
    :param n: Nombre de régions à extraire pour le top et le bottom.
    :return: Deux DataFrames (top_n, bottom_n).
    """
    top_n = moyennes_par_region.sort_values(ascending=False).head(n)
    bottom_n = moyennes_par_region.sort_values(ascending=True).head(n)
    return top_n, bottom_n

def plot_all_regions(moyennes_par_region):
    """
    Crée un graphique pour toutes les régions, triées par leurs moyennes.
    """
    moyennes_par_region.sort_values(ascending=False).plot(
        kind="bar", color="lightblue", figsize=(12, 6)
    )
    plt.title("Entrées moyennes par fauteuil pour toutes les régions (2022)")
    plt.ylabel("Entrées moyennes par fauteuil")
    plt.xlabel("Régions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
