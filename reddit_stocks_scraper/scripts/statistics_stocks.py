# from reddit.models import RedditWallStreetBetsStocksDB
from matplotlib import pyplot as plt
import sqlite3
import pandas as pd

plt.style.use("seaborn")
database = "../db.sqlite3"
database
connection = sqlite3.connect(database)
cursor = connection.cursor()

query_results = cursor.execute(""" SELECT * FROM  reddit_redditwallstreetbetsstocksdb""")
df = pd.DataFrame(query_results)
df.rename(columns={0:"primary_id", 1:"stock_mentions", 2:"stock_ticker"}, inplace=True)

# df is the dataframe containing data from sql
y_axis = df["stock_ticker"]
x_axis = df["stock_mentions"]
print(list(y_axis))
print(list(x_axis))

y_width = []


for i in range(len(y_axis)):
	y_width.append(0.75)

plt.barh(y_axis, x_axis, y_width)
plt.tight_layout()
plt.ylabel("Stock Tickers")
plt.yticks(size="small")
plt.xlabel("Number of Mention")
plt.show()
print(df)