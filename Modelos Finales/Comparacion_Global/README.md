# Comparacion Global de Modelos

## Resumen
Se comparan los cuatro modelos con codigo y ejecucion verificados en el repositorio: Baseline, Naive Bayes,
Logistic Regression y Random Forest.

## Tabla comparativa
| model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| --- | --- | --- | --- | --- | --- |
| Random Forest | 0.9997 | 0.9991 | 0.9991 | 0.9991 | 1.0000 |
| Logistic Regression | 0.9954 | 0.9813 | 0.9946 | 0.9879 | 0.9982 |
| Naive Bayes | 0.8756 | 0.6075 | 0.9676 | 0.7464 | 0.9601 |
| Baseline Classifier | 0.8109 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |

## Ranking por ROC-AUC
| model | ROC-AUC |
| --- | --- |
| Random Forest | 1.0000 |
| Logistic Regression | 0.9982 |
| Naive Bayes | 0.9601 |
| Baseline Classifier | 0.5000 |

## Ranking por F1 Score
| model | F1 Score |
| --- | --- |
| Random Forest | 0.9991 |
| Logistic Regression | 0.9879 |
| Naive Bayes | 0.7464 |
| Baseline Classifier | 0.0000 |

## Figuras
- `figures/comparison_metrics.png`
- `figures/ranking_roc_auc.png`
- `figures/ranking_f1_score.png`

## Errores consolidados
| model | FP | FN | Error Rate | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline Classifier | 0 | 1110 | 0.1891 | 0.0000 | 0.0000 | 0.0000 |
| Naive Bayes | 694 | 36 | 0.1244 | 0.6075 | 0.9676 | 0.7464 |
| Logistic Regression | 21 | 6 | 0.0046 | 0.9813 | 0.9946 | 0.9879 |
| Random Forest | 1 | 1 | 0.0003 | 0.9991 | 0.9991 | 0.9991 |

## Modelo ganador
Por ROC-AUC: **Random Forest**.

Por F1 Score: **Random Forest**.

## Discusion
Los modelos supervisados superan ampliamente al baseline. Random Forest presenta el desempeno global mas alto entre
los modelos verificados, mientras Logistic Regression ofrece una alternativa interpretable con metricas tambien muy
fuertes. Las metricas casi perfectas requieren validacion externa por posible cercania entre target y predictores.

## Estado
Completo: existen rankings, tablas comparativas, metricas consolidadas, README y figuras.
