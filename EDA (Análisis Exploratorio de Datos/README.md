# Exploratory Data Analysis (EDA)

## Objetivo
Analizar el dataset final OSINT, validar la distribucion del target y observar patrones temporales, geograficos,
textuales y multifuente asociados a `regional_escalation_level`.

## Evidencia usada
- Dataset final: `CSVs/Dataset Machine Learning Osint Final.xlsx`.
- Registros: 29,345.
- Columnas tecnicas leidas: 27.
- Figuras generadas: `figures/`.

## Variables creadas verificadas
| variable | existe | nulos | valores_unicos |
| --- | --- | --- | --- |
| text_translated | si | 0 | 29317 |
| sentiment_score | si | 0 | 812 |
| escalation_keyword_score | si | 0 | 7 |
| source_reliability | si | 0 | 6 |
| geo_risk_zone | si | 0 | 3 |
| cross_source_density | si | 0 | 7 |
| severity_proxy | si | 615 | 3387 |

## Distribucion del target
Figura: `figures/target_distribution.png`.

| clase | conteo | porcentaje |
| --- | --- | --- |
| 0 | 23794 | 81.0837 |
| 1 | 5551 | 18.9163 |

El target esta desbalanceado: la clase 0 concentra 81.08% y la clase 1 concentra 18.92%.

## Analisis temporal
Figura: `figures/timeline_escalation.png`.

El pico general ocurre el 2026-05-15 con 6,446 eventos. El pico de alta escalada ocurre el 2026-05-15
con 917 eventos. La alta escalada se concentra en ventanas especificas, por lo que la evaluacion no
debe depender solo de accuracy.

## Analisis geografico
Figura: `figures/risk_map.png`.

Se usaron 8,918 registros con coordenadas validas. La concentracion espacial confirma que la ubicacion y
`geo_risk_zone` aportan senal para la clasificacion.

## Variables creadas vs target
Figura: `figures/escalation_keyword_score_vs_target.png`.

| regional_escalation_level | count | mean | median | std |
| --- | --- | --- | --- | --- |
| 0 | 23794 | 0.0393 | 0.0000 | 0.2843 |
| 1 | 5551 | 1.1218 | 1.0000 | 0.8521 |

Figura: `figures/cross_source_density_vs_target.png`.

| regional_escalation_level | count | mean | median | std |
| --- | --- | --- | --- | --- |
| 0 | 23794 | 4.5924 | 5.0000 | 2.0478 |
| 1 | 5551 | 2.5421 | 1.0000 | 2.3017 |

Figura: `figures/sentiment_score_vs_target.png`.

| regional_escalation_level | count | mean | median | std |
| --- | --- | --- | --- | --- |
| 0 | 23794 | -0.0690 | 0.0000 | 0.2216 |
| 1 | 5551 | -0.4761 | -0.5994 | 0.3830 |

Figura: `figures/source_reliability_vs_target.png`.

| regional_escalation_level | count | mean | median | std |
| --- | --- | --- | --- | --- |
| 0 | 23794 | 0.8874 | 0.9000 | 0.0712 |
| 1 | 5551 | 0.7973 | 0.9000 | 0.1666 |

Figura: `figures/severity_proxy_vs_target.png`.

| regional_escalation_level | count | mean | median | std |
| --- | --- | --- | --- | --- |
| 0 | 23430 | 25.3847 | 31.6600 | 16.4194 |
| 1 | 5300 | 3.5081 | 0.0900 | 8.1506 |

Figura: `figures/geo_risk_zone_by_target.png`.

| geo_risk_zone | 0 | 1 |
| --- | --- | --- |
| high | 3115 | 5192 |
| low | 9747 | 127 |
| medium | 10932 | 232 |

## Correlaciones
Figura: `figures/feature_correlation_matrix.png`.

Correlaciones con el target:

| variable | regional_escalation_level |
| --- | --- |
| regional_escalation_level | 1.0000 |
| escalation_keyword_score | 0.6854 |
| keyword_count | 0.6748 |
| text_length | 0.5363 |
| source_reliability | -0.3425 |
| cross_source_density | -0.3574 |
| severity_proxy | -0.4866 |
| sentiment_score | -0.5229 |

## Hallazgos
- `escalation_keyword_score`, `geo_risk_zone` y `cross_source_density` son senales centrales del target.
- `severity_proxy` y `source_reliability` aportan contexto operativo y calidad relativa de fuente.
- `text_translated` existe como evidencia de normalizacion textual para analisis NLP.
- Las metricas de modelos deben interpretarse con cautela porque el target fue construido con reglas cercanas a algunas
  variables predictoras.

## Estado EDA
Completo: contiene analisis del target, temporal, geografico, variables creadas, correlaciones, hallazgos y figuras.
