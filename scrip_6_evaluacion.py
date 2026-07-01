"""Paso 3: Entrenamiento del Random Forest
Separamos los datos (80% para entrenar, 20% para probar) y le enseñamos a la máquina."""

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Cargar los datos
df = pd.read_pickle('data/processed_ia_dataframe.pkl')

# Definir variables predictoras (X) y objetivo (y)
# Usamos 'rank' y 'month' como predictores de ejemplo
X = df[['rank', 'month']]
y = df['Trend_Class']

# Partición 80/20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo Random Forest
modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

# Hacer predicciones con el 20% de prueba
y_pred = modelo_rf.predict(X_test)
y_prob = modelo_rf.predict_proba(X_test)[:, 1] # Probabilidades para la Curva ROC

print("¡Modelo entrenado exitosamente!")

# Guardamos las variables de prueba y las predicciones para los scripts de métricas
joblib.dump((y_test, y_pred, y_prob), 'data/resultados_modelo.pkl')