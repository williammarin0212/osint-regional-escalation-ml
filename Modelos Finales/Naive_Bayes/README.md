# Naive Bayes

## Descripcion del modelo
Modelo probabilistico simple para verificar senal discriminante OSINT.

## Variables utilizadas
Numericas: `sentiment_score`, `escalation_keyword_score`, `source_reliability`, `cross_source_density`, `keyword_count`, `text_length`, `year`, `month`, `day`, `hour`.

Categoricas: `geo_risk_zone`, `source`, `source_type`, `country`, `region`, `weekday`.

## Configuracion
Particion estratificada 80/20 con `random_state=42`, imputacion de nulos, `ColumnTransformer`, `Pipeline` y
`OneHotEncoder(handle_unknown="ignore")`.

## Metricas
| model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | train_rows | test_rows | target_0 | target_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Naive Bayes | 0.8756 | 0.6075 | 0.9676 | 0.7464 | 0.9601 | 23476 | 5869 | 23794 | 5551 |

## Matriz de confusion
Archivo CSV: `confusion_matrix.csv`.

| real | 0 | 1 |
| --- | --- | --- |
| 0 | 4065 | 694 |
| 1 | 36 | 1074 |

## Figuras
- `figures/confusion_matrix.png`
- `figures/roc_curve.png`


## Analisis de errores
Falsos positivos: 694. Falsos negativos: 36.

Mejora el recall de clase positiva, aunque genera mas falsos positivos que los modelos fuertes.

## Variables mas relevantes
_No aplica o no se genero importancia directa._

## Estado
Completo: tiene codigo, ejecucion reproducible, metricas, figuras, matriz de confusion y documentacion.
