import pandas as pd

def summarize(df):
    return df.describe()

def group_summary(df, column):
    return df.groupby(column).sum().reset_index()
