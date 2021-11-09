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
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_outside:
            list_outside.append(date)

    week_outside=[0, 0, 0, 0]
    for i in list_outside:
        if 2<=i[2]<=8:
            week_outside[0]=week_outside[0]+1
        elif 9<=i[2]<=15:
            week_outside[1]=week_outside[1]+1
        elif 16<=i[2]<=22:
            week_outside[2]=week_outside[2]+1
        elif 23<=i[2]<=29:
            week_outside[3]=week_outside[3]+1
 
    return week_outside

def outside_average(id):
    weekly = outside(id)
    average=(weekly[0]+weekly[1]+weekly[2]+weekly[3])/4

    return average
