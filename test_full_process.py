from src.data_cleaning import load_data, clean_data
from src.analysis import calculate_mean_entries, plot_top_regions
from src.modeling import train_model, evaluate_model
from src.utils import prepare_data
import pandas as pd

file_path = "data/cinemas.csv"
df = load_data(file_path)
df_clean = clean_data(df)

moyennes_par_commune_2021, moyennes_par_commune_2022 = calculate_mean_entries(df_clean)

print("Moyennes par commune (2021) :\n", moyennes_par_commune_2021)
print("Moyennes par commune (2022) :\n", moyennes_par_commune_2022)

plot_top_regions(moyennes_par_commune_2021, moyennes_par_commune_2022)

X_train, X_test, y_train, y_test = prepare_data(df_clean)

model = train_model(X_train, y_train)

r2, mae = evaluate_model(model, X_test, y_test)
print(f"Performance du modèle - R² : {r2}, MAE : {mae}")

ecrans_fictifs = 5  
fauteuils_fictifs = 500  
population_fictive = 10000  

data_fictive = pd.DataFrame([[ecrans_fictifs, fauteuils_fictifs, population_fictive]], 
                            columns=['écrans', 'fauteuils', 'population de la commune'])

entrees_fictives = model.predict(data_fictive)

print(f"Prédiction des entrées pour les données fictives : {entrees_fictives[0]}")
