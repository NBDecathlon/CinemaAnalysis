import pandas as pd
from src.data_cleaning import load_data, clean_data, display_statistics
from src.analysis import calculate_mean_entries, plot_top_regions
from src.modeling import train_model, evaluate_model
from src.utils import prepare_data

file_path = "data/cinemas.csv"
df = load_data(file_path)
df_clean = clean_data(df)
display_statistics(df_clean)

moyennes_par_region_2021, moyennes_par_region_2022 = calculate_mean_entries(df_clean)
plot_top_regions(moyennes_par_region_2021, moyennes_par_region_2022)

X_train, X_test, y_train, y_test = prepare_data(df_clean)

model = train_model(X_train, y_train)
r2, mae = evaluate_model(model, X_test, y_test)
print(f"R² : {r2}, MAE : {mae}")

ecrans_fictifs = 5  
fauteuils_fictifs = 500  
population_fictive = 10000  

entrees_fictives = model.predict([[ecrans_fictifs, fauteuils_fictifs, population_fictive]])
print(f"Prédiction des entrées pour les données fictives : {entrees_fictives}")
