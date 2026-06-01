# Random Forest

## Descripcion del modelo
Ensamble de arboles para capturar interacciones no lineales.

## Variables utilizadas
Numericas: `sentiment_score`, `escalation_keyword_score`, `source_reliability`, `cross_source_density`, `keyword_count`, `text_length`, `year`, `month`, `day`, `hour`.

Categoricas: `geo_risk_zone`, `source`, `source_type`, `country`, `region`, `weekday`.

## Configuracion
Particion estratificada 80/20 con `random_state=42`, imputacion de nulos, `ColumnTransformer`, `Pipeline` y
`OneHotEncoder(handle_unknown="ignore")`.

## Metricas
| model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | train_rows | test_rows | target_0 | target_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Random Forest | 0.9997 | 0.9991 | 0.9991 | 0.9991 | 1.0000 | 23476 | 5869 | 23794 | 5551 |

## Matriz de confusion
Archivo CSV: `confusion_matrix.csv`.

| real | 0 | 1 |
| --- | --- | --- |
| 0 | 4758 | 1 |
| 1 | 1 | 1109 |

## Figuras
- `figures/confusion_matrix.png`
- `figures/roc_curve.png`
- `figures/feature_importance.png`

## Analisis de errores
Falsos positivos: 1. Falsos negativos: 1.

Alcanza el mejor equilibrio entre precision y recall entre los modelos verificados.

## Variables mas relevantes
| feature | importance |
| --- | --- |
| num__escalation_keyword_score | 0.1937 |
| cat__region_LEVANT | 0.1335 |
| cat__geo_risk_zone_high | 0.1302 |
| num__keyword_count | 0.1017 |
| num__text_length | 0.0438 |
| cat__source_nasa_firms | 0.0389 |
| num__sentiment_score | 0.0387 |
| num__cross_source_density | 0.0385 |
| cat__source_type_satellite_detection | 0.0350 |
| cat__country_Israel/Palestine | 0.0266 |

## Estado
Completo: tiene codigo, ejecucion reproducible, metricas, figuras, matriz de confusion y documentacion.
