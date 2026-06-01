# Baseline Classifier

## Descripcion del modelo
Clasificador base que predice siempre la clase mayoritaria.

## Variables utilizadas
Numericas: `sentiment_score`, `escalation_keyword_score`, `source_reliability`, `cross_source_density`, `keyword_count`, `text_length`, `year`, `month`, `day`, `hour`.

Categoricas: `geo_risk_zone`, `source`, `source_type`, `country`, `region`, `weekday`.

## Configuracion
Particion estratificada 80/20 con `random_state=42`, imputacion de nulos, `ColumnTransformer`, `Pipeline` y
`OneHotEncoder(handle_unknown="ignore")`.

## Metricas
| model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | train_rows | test_rows | target_0 | target_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline Classifier | 0.8109 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | 23476 | 5869 | 23794 | 5551 |

## Matriz de confusion
Archivo CSV: `confusion_matrix.csv`.

| real | 0 | 1 |
| --- | --- | --- |
| 0 | 4759 | 0 |
| 1 | 1110 | 0 |

## Figuras
- `figures/confusion_matrix.png`
- `figures/roc_curve.png`


## Analisis de errores
Falsos positivos: 0. Falsos negativos: 1110.

No detecta eventos de alta escalada; sirve solo como referencia minima.

## Variables mas relevantes
_No aplica o no se genero importancia directa._

## Estado
Completo: tiene codigo, ejecucion reproducible, metricas, figuras, matriz de confusion y documentacion.
