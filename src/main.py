import pandas as pd
from src.data_loader import load_excel
from src.analyzer import summarize
from src.visualizer import plot_column
from src.reporter import send_report

def run():
    df = load_excel(["data/sample1.xlsx","data/sample2.xlsx"])
    summary = summarize(df)
    summary.to_excel("reports/summary.xlsx", index=False)

    plot_column(df, df.columns[0], "plots/plot.png")

    send_report(
        "recipient@example.com",
        "Automated Report",
        "Please find attached the automated report.",
        ["reports/summary.xlsx","plots/plot.png"]
    )

if __name__ == "__main__":
    run()
