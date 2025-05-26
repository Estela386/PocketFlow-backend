import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Cargar CSV
csv_path = os.path.join(os.path.dirname(__file__), 'training', 'egresos.csv')
df = pd.read_csv(csv_path)

# Asegurarse de que la fecha es datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Extraer partes de la fecha
df["dia"] = df["fecha"].dt.day
df["semana"] = df["fecha"].dt.isocalendar().week
df["mes"] = df["fecha"].dt.month
df["anio"] = df["fecha"].dt.year

# Columnas para el modelo
features = ["motivo", "semana", "mes", "anio"]
target = "cantidad"

# Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown='ignore'), ["motivo"])]
)

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Entrenamiento
X = df[features]
y = df[target]
pipeline.fit(X, y)

# Guardar modelo
output_path = os.path.join(os.path.dirname(__file__), 'training', 'modelo_egresos.joblib')
joblib.dump(pipeline, output_path)
print(f"Modelo guardado en: {output_path}")

