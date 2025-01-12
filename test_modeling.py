import pandas as pd
from sklearn.model_selection import train_test_split
from src.modeling import train_model, evaluate_model

data = {
    'écrans': [200, 150, 180, 220, 170],
    'fauteuils': [5000, 4000, 4500, 6000, 5200],
    'population de la commune': [100000, 80000, 90000, 120000, 95000],
    'entrées 2022': [520000, 420000, 470000, 580000, 530000]
}

df = pd.DataFrame(data)

X = df[['écrans', 'fauteuils', 'population de la commune']]
y = df['entrées 2022']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = train_model(X_train, y_train)

r2, mae = evaluate_model(model, X_test, y_test)

print(f"R² : {r2}")
print(f"MAE : {mae}")