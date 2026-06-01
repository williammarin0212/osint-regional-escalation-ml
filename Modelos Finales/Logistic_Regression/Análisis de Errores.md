# Analisis de Errores - Logistic Regression

## Resumen
| Indicador | Valor |
| --- | ---: |
| Total de observaciones evaluadas | 5.869 |
| True Positives | 1.104 |
| True Negatives | 4.738 |
| False Positives | 21 |
| False Negatives | 6 |

## Distribucion de errores
| Tipo de error | Total | Porcentaje sobre prueba |
| --- | ---: | ---: |
| False Positives | 21 | 0.36% |
| False Negatives | 6 | 0.10% |
| Error total | 27 | 0.46% |

## Patrones detectados
### source
| source | errores | porcentaje |
| --- | --- | --- |
| youtube | 21 | 0.7778 |
| gdelt | 6 | 0.2222 |

### source_type
| source_type | errores | porcentaje |
| --- | --- | --- |
| video_platform | 21 | 0.7778 |
| news_intelligence | 6 | 0.2222 |

### country
| country | errores | porcentaje |
| --- | --- | --- |
| Iran | 12 | 0.4444 |
| Yemen | 7 | 0.2593 |
| UNKNOWN | 7 | 0.2593 |
| Israel | 1 | 0.0370 |

### geo_risk_zone
| geo_risk_zone | errores | porcentaje |
| --- | --- | --- |
| medium | 19 | 0.7037 |
| low | 7 | 0.2593 |
| high | 1 | 0.0370 |

## Ejemplos representativos

### 5 falsos positivos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 926caf95-6835-458a-9b2f-606e85e7d51a | 19/04/2025 | youtube | video_platform | UNKNOWN | low | 5 | 1 | 0 | 1 | 1.0000 |
| 59fc89a6-138a-41cf-b3d7-3b1633542353 | 21/04/2025 | youtube | video_platform | Yemen | medium | 4 | 1 | 0 | 1 | 1.0000 |
| 079ff519-4de7-401e-aec3-dfe6605b9a8b | 19/03/2025 | youtube | video_platform | Iran | medium | 4 | 1 | 0 | 1 | 0.9999 |
| b118ce48-2a03-4ea3-a95f-88d1825e6126 | 28/07/2025 | youtube | video_platform | Yemen | medium | 3 | 1 | 0 | 1 | 0.9984 |
| 9483cbfb-e3ea-4094-9bbf-b48e218fc963 | 21/04/2025 | youtube | video_platform | Yemen | medium | 3 | 1 | 0 | 1 | 0.9981 |

### 5 falsos negativos representativos
| record_id | date_utc | source | source_type | country | geo_risk_zone | escalation_keyword_score | cross_source_density | regional_escalation_level | predicted_level | prob_high_escalation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| f20f1cce-dfac-4f0a-952d-a1d10d4aa892 | 10/05/2026 | youtube | video_platform | Iran | medium | 1 | 3 | 1 | 0 | 0.0001 |
| 61e76ece-879f-406a-b249-bba3fed9bafd | 10/05/2026 | youtube | video_platform | UNKNOWN | low | 1 | 3 | 1 | 0 | 0.0009 |
| 37d2c2f6-dbc7-48ee-9da7-02511b2b6fff | 11/05/2026 | gdelt | news_intelligence | Iran | medium | 1 | 4 | 1 | 0 | 0.3611 |
| 91e61195-0c09-4e7f-9c1c-42d74e13d383 | 11/05/2026 | gdelt | news_intelligence | Iran | medium | 1 | 4 | 1 | 0 | 0.3729 |
| a04df21a-ca5c-43fb-b33d-337f26bd833e | 11/05/2026 | gdelt | news_intelligence | Iran | medium | 1 | 4 | 1 | 0 | 0.3764 |

## Posibles causas
Los falsos positivos se concentran principalmente en registros de tipo `video_platform`, lo que sugiere senales OSINT intensas que parecen escalada aunque la etiqueta real sea baja. Los falsos negativos aparecen con mayor frecuencia en zona `medium`, indicando eventos de alta escalada que comparten rasgos con actividad regional rutinaria o menos visible. Las variables categoricas de fuente, pais y zona de riesgo pueden inducir confusion cuando un evento tiene alta intensidad textual pero baja etiqueta, o cuando una alta escalada ocurre con senales cuantitativas moderadas.

## Implicaciones
El riesgo principal es sobre-alertar eventos, lo que puede saturar la revision humana y elevar costos de validacion OSINT.

## Conclusion
Logistic Regression ofrece un equilibrio fuerte entre deteccion y control de falsas alarmas.
