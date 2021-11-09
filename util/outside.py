import numpy as np
import pandas as pd
from util import read_file as rf
from util import outsideScore


def outside(id):
    data=rf.read_file(id)

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
        time=mass[1].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        out_time = round((hour+min+sec)/60)
        list_outside.append(out_time)

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
        time=mass[1].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        out_time = round((hour+min+sec)/60)
        list_inside.append(out_time)

    wasOutside=[]

    for i in range(len(list_outside)):
        timeOutside = abs(list_inside[i] - list_outside[i])
        wasOutside.append(timeOutside)

    return wasOutside

def recent_outside(id):
    out_time = outside(id)
    out_length = len(out_time)-1

    if(out_length==0):
        return 0
    else:
        return out_time[out_length]
