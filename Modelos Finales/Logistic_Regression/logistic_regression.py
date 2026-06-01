from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "CSVs" / "Dataset Machine Learning Osint Final.xlsx"
TARGET = "regional_escalation_level"
NUMERIC_FEATURES = [
    "sentiment_score",
    "escalation_keyword_score",
    "source_reliability",
    "cross_source_density",
    "keyword_count",
    "text_length",
    "year",
    "month",
    "day",
    "hour",
]
CATEGORICAL_FEATURES = ["geo_risk_zone", "source", "source_type", "country", "region", "weekday"]


def one_hot_encoder() -> OneHotEncoder:
    params = {"handle_unknown": "ignore"}
    if "sparse_output" in OneHotEncoder.__init__.__code__.co_varnames:
        params["sparse_output"] = True
    else:
        params["sparse"] = True
    return OneHotEncoder(**params)


def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), NUMERIC_FEATURES),
            (
                "cat",
                Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", one_hot_encoder())]),
                CATEGORICAL_FEATURES,
            ),
        ]
    )
    model = LogisticRegression(max_iter=2000, class_weight="balanced", solver="lbfgs")
    return Pipeline([("preprocessor", preprocessor), ("model", model)])


def load_data() -> tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    df = pd.read_excel(DATASET)
    return df[NUMERIC_FEATURES + CATEGORICAL_FEATURES], df[TARGET].astype(int), df


def dashboard_figures_dir() -> Path:
    figures_dir = Path(__file__).resolve().parent / "figures"
    figures_dir.mkdir(exist_ok=True)
    return figures_dir


def save_timeline(df: pd.DataFrame, figures_dir: Path) -> None:
    date_column = "date_utc" if "date_utc" in df.columns else "timestamp_utc"
    timeline = df[[date_column, TARGET]].copy()
    timeline["date"] = pd.to_datetime(timeline[date_column], errors="coerce", dayfirst=True).dt.date
    timeline = timeline.dropna(subset=["date"])
    daily = timeline.groupby(["date", TARGET]).size().unstack(fill_value=0).sort_index()
    daily.index = pd.to_datetime(daily.index)
    for level in [0, 1]:
        if level not in daily.columns:
            daily[level] = 0
    daily = daily[[0, 1]]
    rolling_high = daily[1].rolling(window=7, min_periods=1).mean()

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(daily.index, daily[0], color="#2563eb", linewidth=1.4, label="Baja escalada")
    ax.plot(daily.index, daily[1], color="#dc2626", linewidth=1.6, label="Alta escalada")
    ax.plot(daily.index, rolling_high, color="#111827", linewidth=2.0, label="Promedio movil alta escalada")
    ax.set_title("Timeline de escalada regional")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Eventos registrados")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(figures_dir / "timeline_escalation.png", dpi=180)
    plt.close(fig)


def save_risk_map(df: pd.DataFrame, figures_dir: Path) -> None:
    geo = df[["longitude", "latitude", TARGET]].dropna().copy()
    geo = geo[geo["longitude"].between(-180, 180) & geo["latitude"].between(-90, 90)]
    colors = geo[TARGET].map({0: "#2563eb", 1: "#dc2626"})
    sizes = geo[TARGET].map({0: 10, 1: 24})

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(geo["longitude"], geo["latitude"], c=colors, s=sizes, alpha=0.38, edgecolors="none")
    ax.set_title("Mapa geografico de riesgo")
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(figures_dir / "risk_map.png", dpi=180)
    plt.close(fig)


def save_dashboard_figures(df: pd.DataFrame) -> None:
    figures_dir = dashboard_figures_dir()
    save_timeline(df, figures_dir)
    save_risk_map(df, figures_dir)


def main() -> None:
    X, y, df = load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    y_score = pipeline.predict_proba(X_test)[:, 1]
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, zero_division=0),
        "Recall": recall_score(y_test, y_pred, zero_division=0),
        "F1 Score": f1_score(y_test, y_pred, zero_division=0),
        "ROC-AUC": roc_auc_score(y_test, y_score),
    }
    save_dashboard_figures(df)
    print({key: round(value, 4) for key, value in metrics.items()})


if __name__ == "__main__":
    main()
