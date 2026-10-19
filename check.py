import pandas as pd

watchlist_df = pd.read_csv("watchlist.csv")
print(watchlist_df["code"].tolist())