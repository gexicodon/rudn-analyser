import pandas as pd

def find_risk_students(df: pd.DataFrame, threshold: float = -10) -> pd.DataFrame:
    df = df.copy()

    df = df.sort_values(["student_id", "subject", "date"])

    df["delta"] = (
        df
        .groupby(["student_id", "subject"])["score"]
        .diff()
    )

    risk_df = df[
        (df["delta"].notna()) &
        (df["delta"] <= threshold)
    ]

    return risk_df
