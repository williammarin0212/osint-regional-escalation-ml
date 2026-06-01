# Logistic Regression

## Descripcion del modelo
Modelo lineal interpretable con pesos balanceados.

## Variables utilizadas
Numericas: `sentiment_score`, `escalation_keyword_score`, `source_reliability`, `cross_source_density`, `keyword_count`, `text_length`, `year`, `month`, `day`, `hour`.

Categoricas: `geo_risk_zone`, `source`, `source_type`, `country`, `region`, `weekday`.

## Configuracion
Particion estratificada 80/20 con `random_state=42`, imputacion de nulos, `ColumnTransformer`, `Pipeline` y
`OneHotEncoder(handle_unknown="ignore")`.

## Metricas
| model | Accuracy | Precision | Recall | F1 Score | ROC-AUC | train_rows | test_rows | target_0 | target_1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Logistic Regression | 0.9954 | 0.9813 | 0.9946 | 0.9879 | 0.9982 | 23476 | 5869 | 23794 | 5551 |

## Matriz de confusion
Archivo CSV: `confusion_matrix.csv`.

| real | 0 | 1 |
| --- | --- | --- |
| 0 | 4738 | 21 |
| 1 | 6 | 1104 |

## Figuras
- `figures/confusion_matrix.png`
- `figures/roc_curve.png`
- `figures/feature_importance.png`

## Analisis de errores
Falsos positivos: 21. Falsos negativos: 6.

Ofrece alto desempeno e interpretabilidad; sus coeficientes ayudan a explicar las senales OSINT.

## Variables mas relevantes
| feature | coefficient |
| --- | --- |
| num__cross_source_density | 7.0978 |
| cat__geo_risk_zone_high | 4.9548 |
| cat__region_LEVANT | 4.9548 |
| num__escalation_keyword_score | 4.5154 |
| cat__region_GULF | -3.2999 |
| cat__geo_risk_zone_medium | -3.1511 |
| cat__geo_risk_zone_low | -2.4381 |
| cat__country_UNKNOWN | -2.4381 |
| cat__region_OTHER | -2.4381 |
| cat__country_Iran/Gulf | -2.2250 |

## Estado
Completo: tiene codigo, ejecucion reproducible, metricas, figuras, matriz de confusion y documentacion.
