import med
import numpy as np
import pandas as pd

user_data = pd.read_csv("user_profile.csv", encoding="euc-kr")
IDs = user_data["id"].values.tolist()


def all_med(id):
    avg_div = 0
    for i in len(med(int(id))):
        avg_div += med(int(id))[i]
    avg = avg_div/len(med(int(id)))

    return avg