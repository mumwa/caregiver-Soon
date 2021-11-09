from util import social
import numpy as np
import pandas as pd

user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
IDs = user_data["id"].values.tolist()

def all_social():
    #All people avg_of "social_me"
    all_social=[]
    count=0
    total_average=0
    for id in IDs:
        value=social.social_me(int(id))
        line=[id, value]
        all_social.append(line)
        count=count+1
    for i in all_social:
        total_average=total_average + i[1]
    return total_average/len(all_social)