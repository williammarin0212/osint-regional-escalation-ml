# OSINT Regional Escalation Detection - Machine Learning

## Introducción

Análisis, modelamiento y visualización de eventos relacionados con el conflicto Irán–Israel–EE.UU. mediante la integración de múltiples fuentes OSINT abiertas. El proyecto utiliza técnicas de Ciencia de Datos, NLP y Machine Learning para detectar y clasificar escenarios de escalada regional, apoyándose en información geográfica, textual y temporal proveniente de diferentes fuentes de inteligencia abierta.

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

## Nota

No es necesario ejecutar los notebooks para utilizar el dashboard, ya que los datos, visualizaciones y resultados de los modelos se encuentran integrados dentro de la aplicación desplegada.

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

## Nota

No es necesario ejecutar los notebooks para utilizar el dashboard, ya que los datos, visualizaciones y resultados de los modelos se encuentran integrados dentro de la aplicación desplegada.

