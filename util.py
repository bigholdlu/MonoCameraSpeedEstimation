import pandas as pd
import numpy as np

def findMinLoss(real, predicted):
    df = pd.DataFrame([real, predicted]).T
    df.columns = ["real", "prediction"]
    x = []
    for i in range(20):
        df['rolling_predicton'] = df["prediction"].rolling(window=i).agg('mean').fillna(df["prediction"])
        x.append(((df["rolling_predicton"] - df['real'])**2).mean())
    return np.min(x)


