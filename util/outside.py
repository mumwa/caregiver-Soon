import numpy as np
import pandas as pd
import outsideScore

def read_file(id):
    if(id > 30063):
        file="../data/hs_"+str(id)+"_m08_0903_1356.csv"
    else:
        file="../data/hs_"+str(id)+"_m08_0903_1355.csv"
    data=pd.read_csv(file, encoding="cp949")
    return data


def outside(id):
    data=read_file(id)

    list_outside= []
    out_num= []

    outside= data['Act'].str.contains("외출").tolist()
    count=0
    for out in outside:
        if out==True:
            out_num.append(int(count))
        count=count+1
    for i in out_num:
        mass=data.iloc[i]['Time'].split(' ')
        time=mass[0].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        out_time = hour+min+sec
        list_outside.append(time)

    list_inside= []
    in_num= []

    inside= data['Act'].str.contains("귀가").tolist()
    count=0
    for ins in inside:
        if ins==True:
            in_num.append(int(count))
        count=count+1
    for i in in_num:
        mass=data.iloc[i]['Time'].split(' ')
        time=mass[0].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        out_time = hour+min+sec
        list_inside.append(time)

    wasOutside=[]

    for i in len(out_num):
        timeOutside = list_outside[i] - list_inside[i]
        wasOutside.append(timeOutside)

    return wasOutside
