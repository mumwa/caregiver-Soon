import numpy as np
import pandas as pd
from datetime import datetime
from util import read_file

def emergency(id):
    data=read_file.read_file(id)
    activity_time= data['Time'].tolist()
    list_act=data['Act'].tolist()
    list_time=[]
    emergency=False

    count=0
    for i in activity_time:
            mass=i.split(' ')
            date=mass[0].split('-')
            year=date[0]
            date[0]=year[1:5]
            time=mass[1].split(':')
            one=datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]), int(time[2]))
            list_time.append(one)

    count=0
    for time in list_time:
        if count == len(list_time)-1:
            break
        sub_time=list_time[count+1]-list_time[count]
        if sub_time.days > 1:
            if list_act[count]!="외출":
                emergency=True
        count=count+1
    return emergency