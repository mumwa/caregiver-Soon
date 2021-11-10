from util import med
from util import medScore
import numpy as np
import pandas as pd

user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
IDs = user_data["id"].values.tolist()


def all_med(id):
    avg_div = 0
    my_list = med.med(int(id))
    if(len(my_list)==0):
        return 0
    else:
        for i in range(len(my_list)):
            avg_div = avg_div + my_list[i]
        avg = round(avg_div/len(my_list))
        return avg
