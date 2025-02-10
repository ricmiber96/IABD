# Car Price Prediction Challenge

## 📌 Descripción del Proyecto
Este proyecto tiene como objetivo predecir el precio de diferentes automóviles utilizando **Redes Neuronales**. Para ello, trabajaremos con un conjunto de datos que contiene información relevante sobre los vehículos, como su fabricante, año de producción, tipo de combustible, kilometraje y más.

## 📂 Estructura del Proyecto
```
📁 Car-Price-Prediction
│── 📂 data                  # Datos brutos y preprocesados
│── 📂 notebooks             # Notebooks con el análisis y modelo
│── 📂 models                # Modelos entrenados
│── 📂 reports               # Reportes y visualizaciones
│── 📜 requirements.txt      # Dependencias del proyecto
│── 📜 README.md             # Descripción del proyecto
│── 📜 app.py                # Script para despliegue (opcional)
```

## 📊 Pasos del Proyecto

### 1️⃣ Data Cleaning y Preprocesamiento
- Manejo de valores nulos y duplicados.
- Conversión de variables categóricas a numéricas.
- Normalización y escalado de variables.
- Eliminación de outliers si es necesario.

### 2️⃣ Análisis Exploratorio de Datos (EDA)
- Estadísticas generales del dataset.
- Visualización de correlaciones entre variables.
- Análisis de la distribución de precios.
- Identificación de características clave que afectan el precio.

### 3️⃣ Entrenamiento del Modelo con Redes Neuronales
- Creación de una red neuronal con **TensorFlow/Keras**.
- Configuración de la arquitectura de la red (capas densas, activaciones, dropout, etc.).
- Uso de técnicas como **Batch Normalization y Regularización** para mejorar el rendimiento.
- Evaluación del modelo con métricas como **MAE, RMSE, R²**.

### 4️⃣ Optimización y Selección de Características
- **Hyperparameter Tuning** usando `KerasTuner`.
- Evaluación del impacto de cada variable en el modelo.
- Interpretabilidad mediante **SHAP Values** o análisis de pesos de la red.

### 5️⃣ Despliegue del Modelo (Opcional)
- Guardado del modelo con **TensorFlow SavedModel o H5**.
- Implementación con **Flask, FastAPI o Streamlit**.
- Uso de **MLflow** para el tracking de experimentos.

## 📄 Descripción del Dataset
- **Archivo CSV**: 19,237 filas x 18 columnas
- **Variable Objetivo**: `Price` (Precio del auto)

### **Atributos Principales:**
| Atributo           | Descripción |
|--------------------|-------------|
| ID                | Identificador único |
| Price             | Precio del auto (Objetivo) |
| Levy              | Impuesto anual |
| Manufacturer      | Fabricante |
| Model            | Modelo del auto |
| Prod. year       | Año de fabricación |
| Category         | Tipo de auto |
| Leather interior | Interior de cuero (Sí/No) |
| Fuel type        | Tipo de combustible |
| Engine volume    | Cilindrada del motor |
| Mileage          | Kilometraje |
| Cylinders        | Número de cilindros |
| Gear box type    | Tipo de transmisión |
| Drive wheels     | Tracción (FWD, RWD, AWD) |
| Doors           | Número de puertas |
| Wheel           | Tipo de llantas |
| Color           | Color del auto |
| Airbags         | Número de airbags |

## 📌 Futuras Mejoras
- **Optimización del modelo:** Probar diferentes arquitecturas de redes neuronales.
- **Mejor Feature Engineering:** Crear nuevas variables derivadas.
- **Despliegue Web:** Crear una interfaz de usuario para predicciones en tiempo real.
- **Automatización con MLOps:** Integrar MLflow y CI/CD.

## ⚡ Requerimientos
Para ejecutar este proyecto, instala las dependencias con:
```bash
pip install -r requirements.txt
```

## 🚀 Ejecución del Proyecto
1. Descarga el dataset en la carpeta `data/`.
2. Ejecuta los notebooks en la carpeta `notebooks/`.
3. Entrena el modelo y evalúa su rendimiento.
4. (Opcional) Despliega la API con `python app.py`.

---
Este proyecto sirve como una excelente práctica de redes neuronales con Tensorflow 🧠😎

