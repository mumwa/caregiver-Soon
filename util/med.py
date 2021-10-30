import numpy as np
import pandas as pd
import medAverage
import medScore

def read_file(id):
    if(id > 30063):
        file="../data/hs_"+str(id)+"_m08_0903_1356.csv"
    else:
        file="../data/hs_"+str(id)+"_m08_0903_1355.csv"
    data=pd.read_csv(file, encoding="cp949")
    return data


def med(id):
    data=read_file(id)

    list_med= []
    time_med= []
    meds= []

    meds_boolean= data['State'].str.contains("기상 약 복용" | "복약" | "식후 약 복용").tolist()
    count=0
    for med_bool in meds_boolean:
        if med_bool==True:
            meds.append(int(count))
        count=count+1

    for i in meds:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        list_med.append(date)

    for i in meds:
        mass=data.iloc[i]['Time'].split(' ')
        time=mass[0].split(':')
        hour=int(time[0])*60*60
        min=int(time[1])*60
        sec=int(time[2])
        med_time = hour+min+sec
        time_med.append(med_time)

    med_list=[]

    for i in list_med:
        med_list.append([])
        for j in time_med:
            med_list[i].append(j)

            #여기서 막힘

#dailyaverage = avg of whole day

    return dailyAverage
