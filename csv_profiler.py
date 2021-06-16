import sys
import webbrowser

import pandas as pd
import dtale
from pandas_profiling import ProfileReport

fpath = str(sys.argv[1])
file = str(sys.argv[2]).split(".")[0]

df = pd.read_csv(f"{fpath}/{file}.csv", index_col=False)


def generate(df):
    profile = ProfileReport(df, title=file)
    profile.to_file(f"{fpath}/{file}.html")
    webbrowser.open(f"file://{fpath}/{file}.html")

    dtale.show(df)
    webbrowser.open("http://localhost:40000/dtale/main/1")


if __name__ == "__main__":
    generate(df)
