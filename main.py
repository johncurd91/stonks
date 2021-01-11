import yfinance as yf
import pandas as pd
import numpy as np
import calendar
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels

# Settings
target = "TSLA"
period = "1y"

# Fetch data
df = yf.Ticker(target)
df = df.history(period=period)
df.reset_index(inplace=True)
print(df)

# Plot data
sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=0.8)
sns.lineplot(
    data=df,
    x="Date",
    y="High"
)
sns.lineplot(
    data=df,
    x="Date",
    y="Close"
)
plt.legend(["High", "Close"])
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.show()
