from src.analysis import calculate_mean_entries, plot_top_regions
import pandas as pd

data = {
    'région administrative': [
        'Île-de-France', 'Provence-Alpes-Côte d\'Azur', 'Occitanie', 
        'Auvergne-Rhône-Alpes', 'Nouvelle-Aquitaine',
        'Bourgogne-Franche-Comté', 'Bretagne', 'Centre-Val de Loire',
        'Grand Est', 'Hauts-de-France'
    ],
    'écrans': [200, 150, 180, 220, 170, 130, 140, 160, 190, 210],
    'fauteuils': [5000, 4000, 4500, 6000, 5200, 3100, 3400, 4200, 4700, 5100],
    'entrées 2021': [500000, 400000, 450000, 550000, 520000, 300000, 320000, 400000, 470000, 500000],
    'entrées 2022': [520000, 420000, 470000, 580000, 530000, 310000, 330000, 410000, 480000, 510000]
}

df = pd.DataFrame(data)

moyennes_par_region_2021, moyennes_par_region_2022 = calculate_mean_entries(df)

print("Moyennes par région (2021) :\n", moyennes_par_region_2021)
print("Moyennes par région (2022) :\n", moyennes_par_region_2022)

plot_top_regions(moyennes_par_region_2021, moyennes_par_region_2022)
