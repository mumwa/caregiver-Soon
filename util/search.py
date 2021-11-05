import numpy as np
import pandas as pd

def search(id):
    user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
    IDs = user_data["id"].values.tolist()
    for people in IDs:
        if(id==people):
            return True
    return False