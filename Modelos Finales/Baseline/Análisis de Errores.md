# Analisis de Errores - Baseline Classifier

## Resumen
| Indicador | Valor |
| --- | ---: |
| Total de observaciones evaluadas | 5.869 |
| True Positives | 0 |
| True Negatives | 4.759 |
| False Positives | 0 |
| False Negatives | 1.110 |

## Distribucion de errores
| Tipo de error | Total | Porcentaje sobre prueba |
| --- | ---: | ---: |
| False Positives | 0 | 0.00% |
| False Negatives | 1.110 | 18.91% |
| Error total | 1.110 | 18.91% |

## Patrones detectados
### source
| source | errores | porcentaje |
| --- | --- | --- |
| acled | 437 | 0.3937 |
| youtube | 404 | 0.3640 |
| opensky | 92 | 0.0829 |
| gdelt | 69 | 0.0622 |
| nasa_firms | 65 | 0.0586 |

### source_type
| source_type | errores | porcentaje |
| --- | --- | --- |
| event | 437 | 0.3937 |
| video_platform | 404 | 0.3640 |
| aviation_tracking | 92 | 0.0829 |
| news_intelligence | 69 | 0.0622 |
| satellite_detection | 65 | 0.0586 |

### country
| country | errores | porcentaje |
| --- | --- | --- |
| Palestine | 465 | 0.4189 |
| Israel | 413 | 0.3721 |
| Israel/Palestine | 157 | 0.1414 |
| Iran | 45 | 0.0405 |
| UNKNOWN | 24 | 0.0216 |

### geo_risk_zone
| geo_risk_zone | errores | porcentaje |
| --- | --- | --- |
| high | 1040 | 0.9369 |
| medium | 46 | 0.0414 |
| low | 24 | 0.0216 |

## Ejemplos representativos

### 5 falsos positivos representativos
_No aplica: el modelo no produjo casos de este tipo en el conjunto de prueba._

### 5 falsos negativos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b5271b95-1935-400c-93ef-d34f64b36be8 | 12/05/2026 | nasa_firms | satellite_detection | Israel/Palestine | high | 0 | 6 | 1 | 0 | 0.0000 |
| 53ce5dd6-b6b5-4dbc-aa30-0dcb976b1d6f | 15/05/2026 | gdelt | news_intelligence | Israel | high | 0 | 6 | 1 | 0 | 0.0000 |
| 4b4c8a5b-6ecb-4ed2-a4d1-a0c5d8c0cfca | 3/05/2018 | acled | event | Palestine | high | 1 | 1 | 1 | 0 | 0.0000 |
| 95ebeaf7-850a-43a5-b49a-8bed389798a1 | 14/05/2026 | google_news_rss | news_aggregator | Iran | medium | 1 | 7 | 1 | 0 | 0.0000 |
| e4fce389-a92b-4d51-a862-4b76f9829ff2 | 27/04/2026 | youtube | video_platform | Israel | high | 1 | 1 | 1 | 0 | 0.0000 |

## Posibles causas
Los falsos negativos aparecen con mayor frecuencia en zona `high`, indicando eventos de alta escalada que comparten rasgos con actividad regional rutinaria o menos visible. Las variables categoricas de fuente, pais y zona de riesgo pueden inducir confusion cuando un evento tiene alta intensidad textual pero baja etiqueta, o cuando una alta escalada ocurre con senales cuantitativas moderadas.

## Implicaciones
El riesgo principal es omitir episodios de alta escalada, lo que reduce utilidad para alerta temprana y monitoreo preventivo.

## Conclusion
Baseline Classifier no es adecuado para detectar escaladas regionales porque omite todos los eventos positivos.
