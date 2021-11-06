from util import med
import numpy as np
import pandas as pd

user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
IDs = user_data["id"].values.tolist()


def all_med(id):

    avg_div = 0
    my_list = med.med(int(id))
    for i in len(my_list):
        avg_div += my_list[i]
    avg = avg_div/len(my_list)

    return avg