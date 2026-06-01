# Analisis Global de Errores

## Comparacion de errores entre modelos
| model | TP | TN | FP | FN | Error Rate | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline Classifier | 0 | 4759 | 0 | 1110 | 0.1891 | 0.0000 | 0.0000 | 0.0000 |
| Naive Bayes | 1074 | 4065 | 694 | 36 | 0.1244 | 0.6075 | 0.9676 | 0.7464 |
| Logistic Regression | 1104 | 4738 | 21 | 6 | 0.0046 | 0.9813 | 0.9946 | 0.9879 |
| Random Forest | 1109 | 4758 | 1 | 1 | 0.0003 | 0.9991 | 0.9991 | 0.9991 |

## Lectura
El baseline concentra el riesgo en falsos negativos porque predice siempre baja escalada. Naive Bayes aumenta la
sensibilidad, pero produce mas falsos positivos. Logistic Regression y Random Forest reducen ambos tipos de error.

## Mejor equilibrio
El mejor equilibrio observado corresponde a **Random Forest**, con F1 Score de 0.9991.

## Advertencia metodologica
Las metricas muy altas deben interpretarse con cautela porque el target fue construido con reglas relacionadas con
algunas variables predictoras. La validacion futura deberia usar periodos posteriores o datos externos.
