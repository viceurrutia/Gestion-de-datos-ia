# 📈 Gestión de Datos para IA: Análisis de Google Trends

## 1. Descripción del Proyecto
Este sistema automatiza la extracción, transformación y análisis de datos provenientes del dataset público de Google Trends. El objetivo principal es identificar términos de búsqueda con alto potencial de crecimiento mediante el uso de modelos de Machine Learning, sirviendo como herramienta de apoyo para la toma de decisiones estratégicas.

## 2. Estructura del Repositorio
Para mantener un orden lógico y escalable, el proyecto se divide en los siguientes directorios:

```text
📦 google-trends-ia
 ┣ 📂 sql/                  # Scripts de transformación DML/DDL para capas Silver y Gold
 ┣ 📂 ml_models/            # Consultas de entrenamiento y predicción para BigQuery ML
 ┣ 📂 api/                  # Código fuente del microservicio (FastAPI)
 ┣ 📂 docs/                 # Diagramas de arquitectura, DFD y diccionario de datos
 ┣ 📂 eda/                  # Notebooks de Jupyter con el Análisis Exploratorio de Datos
 ┣ 📜 .env.example          # Plantilla de variables de entorno
 ┣ 📜 requirements.txt      # Dependencias de Python
 ┗ 📜 README.md             # Documentación principal
