import sys
import webbrowser
import pandas as pd
import snowflake.connector
import dtale

from pandas_profiling import ProfileReport
from credentials import SnowflakeConfigs

# query = sys.argv[1]
print("query: ")
query = input()
fpath = str(sys.argv[1])


def generate(query):

    with snowflake.connector.connect(
        authenticator="externalbrowser",
        user=SnowflakeConfigs.USER,
        account=SnowflakeConfigs.ACCOUNT,
        database=SnowflakeConfigs.DATABASE,
        warehouse=SnowflakeConfigs.WAREHOUSE,
        role=SnowflakeConfigs.ROLE,
    ) as conn:
        cur = conn.cursor()
        cur.execute(query)
        cur.get_results_from_sfqid(cur.sfqid)
        results = cur.fetchall()
        col_name = [i[0] for i in cur.description]

    df = pd.DataFrame(
        data=results,
        columns=col_name
    )

    profile = ProfileReport(df, title="query")
    profile.to_file(f"{fpath}/query.html")
    webbrowser.open(f"file://{fpath}/query.html")

    dtale.show(df)
    webbrowser.open("http://localhost:40000/dtale/main/1")


if __name__ == "__main__":
    generate(query)
