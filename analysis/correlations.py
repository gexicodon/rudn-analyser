import pandas as pd

def correlations(df):
    return df.corr(numeric_only=True)
