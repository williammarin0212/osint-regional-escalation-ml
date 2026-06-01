# Analisis de Errores - Random Forest

## Resumen
| Indicador | Valor |
| --- | ---: |
| Total de observaciones evaluadas | 5.869 |
| True Positives | 1.109 |
| True Negatives | 4.758 |
| False Positives | 1 |
| False Negatives | 1 |

## Distribucion de errores
| Tipo de error | Total | Porcentaje sobre prueba |
| --- | ---: | ---: |
| False Positives | 1 | 0.02% |
| False Negatives | 1 | 0.02% |
| Error total | 2 | 0.03% |

## Patrones detectados
### source
| source | errores | porcentaje |
| --- | --- | --- |
| google_news_rss | 1 | 0.5000 |
| youtube | 1 | 0.5000 |

### source_type
| source_type | errores | porcentaje |
| --- | --- | --- |
| news_aggregator | 1 | 0.5000 |
| video_platform | 1 | 0.5000 |

### country
| country | errores | porcentaje |
| --- | --- | --- |
| Iran | 1 | 0.5000 |
| UNKNOWN | 1 | 0.5000 |

### geo_risk_zone
| geo_risk_zone | errores | porcentaje |
| --- | --- | --- |
| medium | 1 | 0.5000 |
| low | 1 | 0.5000 |

## Ejemplos representativos

### 5 falsos positivos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| e2712e32-25cb-45df-9d54-4c4a9b577d95 | 8/05/2026 | google_news_rss | news_aggregator | Iran | medium | 2 | 2 | 0 | 1 | 0.5597 |

### 5 falsos negativos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6b76018e-3f1e-4de8-8cc1-b9a9c53cdce9 | 14/05/2026 | youtube | video_platform | UNKNOWN | low | 1 | 6 | 1 | 0 | 0.4436 |

## Posibles causas
Los falsos positivos se concentran principalmente en registros de tipo `news_aggregator`, lo que sugiere senales OSINT intensas que parecen escalada aunque la etiqueta real sea baja. Los falsos negativos aparecen con mayor frecuencia en zona `low`, indicando eventos de alta escalada que comparten rasgos con actividad regional rutinaria o menos visible. Las variables categoricas de fuente, pais y zona de riesgo pueden inducir confusion cuando un evento tiene alta intensidad textual pero baja etiqueta, o cuando una alta escalada ocurre con senales cuantitativas moderadas.

## Implicaciones
El modelo mantiene un balance simetrico entre falsas alarmas y omisiones, util si se busca equilibrio operativo.

## Conclusion
Random Forest ofrece un equilibrio fuerte entre deteccion y control de falsas alarmas.
