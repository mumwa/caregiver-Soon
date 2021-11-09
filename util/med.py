import numpy as np
import pandas as pd
from util import medAverage
from util import medScore
from util import read_file

#복용 시간 간격 평균 array를 return 
def med(id):
    data=read_file.read_file(id)

    list_calendar = []
    list_med = []
    time_med = []
    meds = []

    meds_boolean= data['State'].str.contains("기상 약 복용|복약|식후 약 복용").tolist()
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
        time=mass[1].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        med_time = round((hour+min+sec)/3600)
        time_med.append(med_time)
    
    daily = []

    for i in range(len(list_med)):
        daily.append([])
        for j in range(list_med.count(list_med[i])):
            daily[i].append(time_med[i+j])

    #calculate daily AVERAGE
    dailyAverage  = []
    avg=0
    for i in range(len(daily)):
        avg = daily[i][len(daily[i])-1] - daily[i][0]
        if(len(daily[i])==0):
            avg=0
        else:
            avg = avg/len(daily[i])
        dailyAverage.append(avg)
        # code with error. never mind
        # for j in daily[i]:
        #    avg+=daily[i][j]
        #avg = avg/len(daily[i])
        #dailyAverage.append(avg)

#dailyaverage = avg of whole day

    return dailyAverage


def recent_med(id):
    list = med(int(id))
    length = len(list)

    if(length>1):
        return list[length-1]
    else:
        return 0
