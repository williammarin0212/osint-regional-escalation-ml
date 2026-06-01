# OSINT Regional Escalation Detection - Machine Learning

## Introducción

Sistema de inteligencia multifuente basado en técnicas de OSINT (Open-Source Intelligence), Procesamiento de Lenguaje Natural (NLP) y Machine Learning para detectar, clasificar y analizar episodios de escalada regional en el conflicto Irán–Israel–EE.UU.

El proyecto integra múltiples fuentes abiertas de información, incluyendo eventos de conflicto, noticias, datos geoespaciales, movilidad aérea y marítima, y señales provenientes de plataformas digitales. A partir de estos datos se construye un dataset unificado que permite analizar patrones asociados a escenarios de alta y baja escalada regional.

Además, se desarrolló un dashboard interactivo para explorar los datos, visualizar hallazgos, comparar modelos de Machine Learning y comunicar los principales resultados obtenidos durante la investigación.

---

## Pregunta de Investigación

> ¿Hasta qué punto un conjunto de fuentes abiertas y gratuitas permite detectar, clasificar o modelar episodios de escalada regional en el conflicto Irán–Israel–EE.UU.?

---

## Integrantes

Valentina Bello Olarte ([valentina.bello1@est.uexternado.edu.co](mailto:valentina.bello1@est.uexternado.edu.co))

William Gómez Marín ([william.gomez3@est.uexternado.edu.co](mailto:william.gomez3@est.uexternado.edu.co))

---

## Dashboard Desplegado

URL del dashboard:

(https://osintregionalescalationdetection.netlify.app/)

---


## Fuentes de Datos

El proyecto integra información procedente de múltiples fuentes OSINT abiertas:

* ACLED
* GDELT
* RSS News
* OpenSky Network
* AISStream
* NASA FIRMS
* Bluesky
* YouTube

Estas fuentes aportan información complementaria sobre eventos de conflicto, cobertura mediática, actividad geoespacial, movilidad y conversación digital.

---

## Dataset

### Archivo principal

```text
Dataset Machine Learning Osint Final.xlsx
```

### Dimensiones

```text
29.345 registros
26 variables
```

### Variable Objetivo

```text
regional_escalation_level
```

Donde:

```text
0 = Baja escalada regional
1 = Alta escalada regional
```

---

## Modelos Implementados

Se desarrollaron y compararon los siguientes modelos de Machine Learning:

* Baseline
* Naive Bayes
* Logistic Regression
* Random Forest

La evaluación se realizó utilizando:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

---

## Instrucciones para Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_REPOSITORIO]
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Abrir Jupyter Notebook

```bash
jupyter notebook
```

### 4. Ejecutar los análisis

Se recomienda seguir el siguiente orden:

#### EDA

Análisis exploratorio de datos:

* distribución del target
* análisis temporal
* análisis geográfico
* correlaciones
* análisis de variables creadas

#### Modelos

Entrenamiento y evaluación de:

* Baseline
* Naive Bayes
* Logistic Regression
* Random Forest

#### Comparación Global

Comparación de métricas y selección del modelo con mejor desempeño.

---

## Dashboard

El dashboard permite:

* Explorar eventos del conflicto.
* Visualizar patrones temporales y geográficos.
* Analizar variables de investigación.
* Comparar resultados de modelos.
* Consultar métricas de desempeño.
* Revisar hallazgos y limitaciones del estudio.

---

## Tecnologías Utilizadas

### Ciencia de Datos y Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Seaborn

### NLP

* TextBlob
* NLTK

### Visualización

* Plotly
* Leaflet / Folium
* Chart.js

### Dashboard

* HTML
* CSS
* JavaScript

---

Proyecto académico desarrollado para la asignatura de Machine Learning y Ciencia de Datos.

Universidad Externado de Colombia.
