from pathlib import Path

import pandas as pd


OUTPUT_DIR = Path(__file__).resolve().parent
TABLE_PATH = OUTPUT_DIR / "tabla_comparativa_modelos.csv"
VARIABLES_PATH = OUTPUT_DIR / "ranking_variables_global.csv"
METRIC_COLUMNS = ["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"]


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    formatted = df.copy()
    for column in formatted.columns:
        if pd.api.types.is_float_dtype(formatted[column]):
            formatted[column] = formatted[column].map(lambda value: f"{value:.4f}")
    lines = [
        "| " + " | ".join(formatted.columns.astype(str)) + " |",
        "| " + " | ".join(["---"] * len(formatted.columns)) + " |",
    ]
    for _, row in formatted.iterrows():
        lines.append("| " + " | ".join(str(row[column]) for column in formatted.columns) + " |")
    return "\n".join(lines)


def write_readme(df: pd.DataFrame, ranking_auc: pd.DataFrame, ranking_f1: pd.DataFrame, variables: pd.DataFrame) -> None:
    winner_auc = ranking_auc.iloc[0]["model"]
    winner_f1 = ranking_f1.iloc[0]["model"]
    winner = winner_auc if winner_auc == winner_f1 else f"{winner_auc} por ROC-AUC; {winner_f1} por F1 Score"
    variable_text = dataframe_to_markdown(variables.head(15)) if not variables.empty else "_Sin ranking disponible._"

    content = f"""# Comparacion Global de Modelos

## 1. Resumen ejecutivo
Se comparan modelos supervisados para clasificar episodios de baja y alta escalada regional en el conflicto
Iran-Israel-EE.UU. Todos usan la misma particion estratificada, las mismas variables predictoras y metricas comunes.

## 2. Comparacion de todos los modelos
{dataframe_to_markdown(df[["model", *METRIC_COLUMNS]])}

## 3. Ranking por ROC-AUC
{dataframe_to_markdown(ranking_auc[["model", "ROC-AUC"]])}

## 4. Ranking por F1 Score
{dataframe_to_markdown(ranking_f1[["model", "F1 Score"]])}

## 5. Discusion metodologica
El flujo metodologico usa imputacion de nulos, OneHotEncoding para variables categoricas, `ColumnTransformer`,
`Pipeline`, `train_test_split(test_size=0.2, stratify=y, random_state=42)` y evaluacion con Accuracy, Precision,
Recall, F1 Score y ROC-AUC. Logistic Regression y Random Forest incorporan `class_weight="balanced"` por el desbalance
moderado del target.

Advertencia metodologica: las metricas casi perfectas deben discutirse con cautela. Si la variable objetivo fue
derivada con reglas cercanas a los predictores, el resultado puede medir consistencia interna del etiquetado mas que
capacidad prospectiva sobre eventos realmente no vistos.

## 6. Modelo ganador
Modelo ganador: **{winner}**.

## 7. Variables mas relevantes
{variable_text}

## 8. Interpretacion geopolitica
Las variables de densidad entre fuentes, puntajes de escalada, zonas de riesgo y region sugieren que la escalada
regional puede modelarse mediante senales OSINT agregadas. Estas senales deben interpretarse como indicadores
operativos, no como causalidad directa.

## 9. Respuesta preliminar a la pregunta de investigacion
Las fuentes abiertas y gratuitas permiten detectar y modelar episodios de escalada regional cuando las senales
estructuradas de texto, fuente, geografia y tiempo superan al baseline en F1, recall y ROC-AUC.
"""
    (OUTPUT_DIR / "README.md").write_text(content, encoding="utf-8")


def main() -> None:
    if not TABLE_PATH.exists():
        raise FileNotFoundError(f"No existe la tabla comparativa final: {TABLE_PATH}")

    df = pd.read_csv(TABLE_PATH).sort_values("ROC-AUC", ascending=False).reset_index(drop=True)
    ranking_auc = df.sort_values("ROC-AUC", ascending=False).reset_index(drop=True)
    ranking_f1 = df.sort_values("F1 Score", ascending=False).reset_index(drop=True)
    variables = pd.read_csv(VARIABLES_PATH) if VARIABLES_PATH.exists() else pd.DataFrame()

    ranking_auc.to_csv(OUTPUT_DIR / "ranking_roc_auc.csv", index=False)
    ranking_f1.to_csv(OUTPUT_DIR / "ranking_f1_score.csv", index=False)
    write_readme(df, ranking_auc, ranking_f1, variables)
    print("Comparacion global actualizada.")


if __name__ == "__main__":
    main()
