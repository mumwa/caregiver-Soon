from util import clean
import numpy as np
import pandas as pd

user_data = pd.read_csv("util/user_profile.csv", encoding="euc-kr")
IDs = user_data["id"].values.tolist()

def all_clean():
    all_clean=[]
    count=0
    total_average=0
    for id in IDs:
        value=clean.clean(int(id))
        line=[id, value]
        all_clean.append(line)
        count=count+1
    for i in all_clean:
        total_average=total_average+i[1]
    return total_average/len(all_clean)

def all_wash():
    all_wash=[]
    count=0
    total_average=0
    for id in IDs:
        value=clean.wash(int(id))
        line=[id, value]
        all_wash.append(line)
        count=count+1
    for i in all_wash:
        total_average=total_average+i[1]
    return total_average/len(all_wash)

def all_fresh():
    all_fresh=[]
    count=0
    total_average=0
    for id in IDs:
        value=clean.fresh(int(id))
        line=[id, value]
        all_fresh.append(line)
        count=count+1
    for i in all_fresh:
        total_average=total_average+i[1]
    return total_average/len(all_fresh)