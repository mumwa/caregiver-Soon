import numpy as np
import pandas as pd
from util import medAverage
from util import medScore
from util import read_file


def med(id):
    data=read_file.read_file(id)

    list_calendar = []
    list_med = []
    time_med = []
    meds = []

    meds_boolean= data['State'].str.contains("기상 약 복용" | "복약" | "식후 약 복용").tolist()
    count=0
    for med_bool in meds_boolean:
        if med_bool==True:
            meds.append(int(count))
        count=count+1

   #for counting days

    for i in meds:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_calendar:
            list_calendar.append(date)
    
    #for counting numbers in a day

    for i in meds:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        list_med.append(date)

    #for calculating time span
    for i in meds:
        mass=data.iloc[i]['Time'].split(' ')
        time=mass[0].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        med_time = hour+min+sec
        time_med.append(med_time)
    
    daily = []

    for i in len(list_med):
        daily.append([])
        for j in list_med[i].count():
            daily[i].append(time_med[i+j])

    #calculate daily AVERAGE
    dailyAverage  = []
    avg=0
    for i in daily:
        for j in daily[i]:
            avg+=daily[i][j]
        dailyAverage.append(avg)

#dailyaverage = avg of whole day

    return dailyAverage
