import pandas as pd

REQUIRED_COLUMNS = {"student_id", "subject", "date", "score", "attendance"}


def validate_frame(df: pd.DataFrame):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f'Отсутсвуют следующие столбцы: {missing}')


def preprocess(df: pd.DataFrame):
    df = df.copy()

    keep_cols = list(REQUIRED_COLUMNS)
    df = df[keep_cols]

    df["student_id"] = pd.to_numeric(df["student_id"], errors="coerce").astype("Int64")
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce").astype("Int64")
    df["date"] = pd.to_datetime(df["date"], format="%d.%m.%y", errors="coerce")
    df = df.dropna(subset=["score"])

    df = df.sort_values(["student_id", "date"]).reset_index(drop=True)


    return df
