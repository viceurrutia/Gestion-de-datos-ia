1. Descripción del Proyecto
Este sistema automatiza la extracción, transformación y análisis de datos provenientes del dataset público de Google Trends en BigQuery. El objetivo es identificar términos con alto potencial de crecimiento mediante modelos de Machine Learning para apoyar la toma de decisiones estratégicas de marketing.
2. Arquitectura Seleccionada
Se implementó una arquitectura de Data Lakehouse sobre Google Cloud Platform (GCP).
Utiliza una Estructura Medallion (Bronze, Silver, Gold) para garantizar la calidad del dato.
La computación se realiza de forma serverless en BigQuery para asegurar escalabilidad total.
3. Requisitos y Configuración del Entorno Técnico
Para replicar o contribuir a este proyecto, se requiere:
Google Cloud SDK: Instalado y autenticado (gcloud auth login).
Python 3.9+: Para la ejecución de scripts de integración.
Librerías Python: google-cloud-bigquery, pandas, pyarrow.
Permisos IAM: Rol de BigQuery Data Viewer para el dataset público y BigQuery Admin para el proyecto local.
Docker: Para desplegar el microservicio del API Gateway.
4. Instrucciones de Instalación
Clonar el repositorio:
Bash
git clone https://github.com/usuario/google-trends-ia.git
cd google-trends-ia
Configurar variables de entorno: Crear un archivo .env con el PROJECT_ID y la ruta a las GOOGLE_APPLICATION_CREDENTIALS.
Ejecutar Pipeline Inicial: Correr el script main.py para crear las vistas filtradas en la Capa Silver.
5. Estructura del Repositorio
/sql: Contiene los scripts de transformación (DML/DDL) para las capas Silver y Gold.
/ml_models: Archivos de entrenamiento de BigQuery ML para predicción de score.
/api: Código fuente en FastAPI para el API Gateway.
/docs: Diagramas de arquitectura y diccionario de datos detallado.
README.md: Documentación principal (este archivo).