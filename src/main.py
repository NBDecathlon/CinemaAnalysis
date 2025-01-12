import pandas as pd
from src.data_cleaning import load_data, clean_data, display_statistics
from src.analysis import calculate_mean_entries, plot_top_regions, get_top_and_bottom_regions, plot_all_regions
from src.modeling import train_model, evaluate_model
from src.utils import prepare_data

file_path = "data/cinemas.csv"
df = load_data(file_path)
df_clean = clean_data(df)
display_statistics(df_clean)

moyennes_par_region_2021, moyennes_par_region_2022 = calculate_mean_entries(df_clean)

top_3, bottom_3 = get_top_and_bottom_regions(moyennes_par_region_2022)

print("Top 3 régions avec les meilleures entrées moyennes (2022) :\n", top_3)
print("Bottom 3 régions avec les pires entrées moyennes (2022) :\n", bottom_3)

plot_top_regions(moyennes_par_region_2021, moyennes_par_region_2022)

plot_all_regions(moyennes_par_region_2022)