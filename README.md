# OSINT Regional Escalation Detection - Machine Learning

## Introducción

Análisis, modelamiento y visualización de eventos relacionados con el conflicto Irán–Israel–EE.UU. mediante la integración de múltiples fuentes OSINT abiertas. El proyecto utiliza técnicas de Ciencia de Datos, NLP y Machine Learning para detectar y clasificar escenarios de escalada regional a partir de señales geográficas, temporales y textuales.

---

## Integrantes

Valentina Bello Olarte ([valentina.bello1@est.uexternado.edu.co](mailto:valentina.bello1@est.uexternado.edu.co))

William Gómez Marín ([william.gomez3@est.uexternado.edu.co](mailto:william.gomez3@est.uexternado.edu.co))

---

## Dashboard Desplegado

```text
https://osintregionalescalationdetection.netlify.app/
```

---

## Pregunta de Investigación

> ¿Hasta qué punto un conjunto de fuentes abiertas y gratuitas permite detectar, clasificar o modelar episodios de escalada regional en el conflicto Irán–Israel–EE.UU.?

---

## Dataset Utilizado

Archivo principal:

```text
Dataset Machine Learning Osint Final.xlsx
```

Registros:

```text
29.345
```

Variable objetivo:

```text
regional_escalation_level

0 = Baja escalada regional
1 = Alta escalada regional
```

---

## Modelos Implementados

* Baseline
* Naive Bayes
* Logistic Regression
* Random Forest

Métricas evaluadas:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## Fuentes de Datos

* ACLED
* GDELT
* RSS News
* OpenSky Network
* AISStream
* NASA FIRMS
* Bluesky
* YouTube

---

## Estructura del Repositorio

```text
Dashboard/
    Dashboard interactivo del proyecto

EDA (Análisis Exploratorio de Datos)/
    Visualizaciones, análisis y hallazgos

Fuente de Datos Final/
    Dataset final utilizado para el proyecto

Modelos Finales/
    Baseline
    Naive Bayes
    Logistic Regression
    Random Forest
    Comparación Global
```

---

## Objetivo del Proyecto

Evaluar el potencial de las fuentes OSINT abiertas para identificar patrones asociados a escenarios de escalada regional y analizar qué tan efectivas resultan para tareas de clasificación supervisada mediante Machine Learning.

---

## Nota

No es necesario ejecutar notebooks o scripts para explorar los resultados principales. El dashboard integra las visualizaciones, métricas, análisis y resultados generados durante el proyecto.
