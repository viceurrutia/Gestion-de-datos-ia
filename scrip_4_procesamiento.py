"""
Fase 1: Análisis de Calidad, Preprocesamiento y Análisis Exploratorio
Extrae la Capa Gold desde PostgreSQL, crea la variable categórica 'Trend_Class' 
y genera la Matriz de Correlación.
"""

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Conexión a tu BD en Docker
engine = create_engine('postgresql://admin:adminpassword@localhost:5432/google_trends_db')
df = pd.read_sql("SELECT * FROM international_top_terms_cl", engine)

# 2. Preprocesamiento: Crear la clase objetivo (Clasificación Binaria)
df['Trend_Class'] = (df['score'] >= 50).astype(int)

# Extraer el mes de la fecha para tener otra variable numérica
df['week'] = pd.to_datetime(df['week'])
df['month'] = df['week'].dt.month

print("Datos listos. Filas totales:", len(df))

# --- GENERACIÓN DE FOTO 1: Matriz de Correlación ---
columnas_numericas = df[['score', 'rank', 'month', 'Trend_Class']]
matriz_corr = columnas_numericas.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación - Tendencias Chile')
plt.show()

# -> SÁQUENLE PANTALLAZO A ESTE GRÁFICO PARA EL WORD <-

# Guardamos el DataFrame listo para que lo use el script de entrenamiento
df.to_pickle('data/dataset_preprocesado.pkl')