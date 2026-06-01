from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from auditoria_finalizacion import generate_eda, load_dataset  # noqa: E402


def main() -> None:
    df = load_dataset()
    generate_eda(df)
    print(f"EDA completo generado en: {Path(__file__).resolve().parent}")


if __name__ == "__main__":
    main()
