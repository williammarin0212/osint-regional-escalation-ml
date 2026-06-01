# Analisis de Errores - Naive Bayes

## Resumen
| Indicador | Valor |
| --- | ---: |
| Total de observaciones evaluadas | 5.869 |
| True Positives | 1.074 |
| True Negatives | 4.065 |
| False Positives | 694 |
| False Negatives | 36 |

## Distribucion de errores
| Tipo de error | Total | Porcentaje sobre prueba |
| --- | ---: | ---: |
| False Positives | 694 | 11.82% |
| False Negatives | 36 | 0.61% |
| Error total | 730 | 12.44% |

## Patrones detectados
### source
| source | errores | porcentaje |
| --- | --- | --- |
| acled | 538 | 0.7370 |
| youtube | 147 | 0.2014 |
| gdelt | 32 | 0.0438 |
| bluesky | 4 | 0.0055 |
| google_news_rss | 4 | 0.0055 |

### source_type
| source_type | errores | porcentaje |
| --- | --- | --- |
| event | 538 | 0.7370 |
| video_platform | 147 | 0.2014 |
| news_intelligence | 32 | 0.0438 |
| news | 5 | 0.0068 |
| social_media | 4 | 0.0055 |

### country
| country | errores | porcentaje |
| --- | --- | --- |
| Palestine | 547 | 0.7493 |
| Israel | 91 | 0.1247 |
| Iran | 56 | 0.0767 |
| UNKNOWN | 35 | 0.0479 |
| Yemen | 1 | 0.0014 |

### geo_risk_zone
| geo_risk_zone | errores | porcentaje |
| --- | --- | --- |
| high | 638 | 0.8740 |
| medium | 57 | 0.0781 |
| low | 35 | 0.0479 |

## Ejemplos representativos

### 5 falsos positivos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9b6c72bb-1843-4a83-8f8f-8e5ed3f7bfde | 30/03/2019 | acled | event | Palestine | high | 0 | 1 | 0 | 1 | 1.0000 |
| 610c569b-ca91-494f-a674-e227a2653e10 | 29/03/2026 | youtube | video_platform | Israel | high | 0 | 1 | 0 | 1 | 1.0000 |
| 09861c6e-d37e-4be1-902a-64e3a2fa7961 | 3/07/2016 | acled | event | Palestine | high | 0 | 1 | 0 | 1 | 1.0000 |
| fcbab723-7b46-4c65-9b68-7c7cecf2dd20 | 7/04/2018 | acled | event | Palestine | high | 0 | 1 | 0 | 1 | 1.0000 |
| 3b2d8fc0-5c8b-4f7e-a9bd-eeb19db06481 | 25/06/2025 | youtube | video_platform | Israel | high | 0 | 1 | 0 | 1 | 1.0000 |

### 5 falsos negativos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49b1b56a-3527-4f3e-b4a5-479015ae6dad | 14/05/2026 | gdelt | news_intelligence | Yemen | medium | 1 | 3 | 1 | 0 | 0.0000 |
| b7e7a434-0f60-4608-9b76-2bb924eff3d8 | 15/05/2026 | gdelt | news_intelligence | UNKNOWN | low | 1 | 6 | 1 | 0 | 0.0000 |
| 2e811673-3baa-406c-89bb-33bb29baf64c | 15/05/2026 | gdelt | news_intelligence | UNKNOWN | low | 1 | 6 | 1 | 0 | 0.0000 |
| 6ab5152c-761e-4d8b-8e87-fe749939c4db | 15/05/2026 | gdelt | news_intelligence | UNKNOWN | low | 1 | 6 | 1 | 0 | 0.0000 |
| 2baed5d7-8b03-4c34-b810-315ae346da68 | 15/05/2026 | gdelt | news_intelligence | UNKNOWN | low | 1 | 6 | 1 | 0 | 0.0000 |

## Posibles causas
Los falsos positivos se concentran principalmente en registros de tipo `event`, lo que sugiere senales OSINT intensas que parecen escalada aunque la etiqueta real sea baja. Los falsos negativos aparecen con mayor frecuencia en zona `low`, indicando eventos de alta escalada que comparten rasgos con actividad regional rutinaria o menos visible. Las variables categoricas de fuente, pais y zona de riesgo pueden inducir confusion cuando un evento tiene alta intensidad textual pero baja etiqueta, o cuando una alta escalada ocurre con senales cuantitativas moderadas.

## Implicaciones
El riesgo principal es sobre-alertar eventos, lo que puede saturar la revision humana y elevar costos de validacion OSINT.

## Conclusion
Naive Bayes es sensible para detectar alta escalada, pero requiere revision humana por su volumen de falsos positivos.
