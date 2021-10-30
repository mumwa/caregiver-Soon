import cleanAverage
import read_file as rf
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

def fresh(id):
    data=rf.read_file(id)

    list_fresh= []
    freshs= []

    freshs_boolean= data['State'].str.contains("집 환기하기").tolist()
    count=0
    for fresh_bool in freshs_boolean:
        if fresh_bool==True:
            freshs.append(int(count))
        count=count+1
    for i in freshs:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_fresh:
            list_fresh.append(date)

    week_fresh=[0, 0, 0, 0]
    for i in list_fresh:
        if 2<=i[2]<=8:
            week_fresh[0]=week_fresh[0]+1
        elif 9<=i[2]<=15:
            week_fresh[1]=week_fresh[1]+1
        elif 16<=i[2]<=22:
            week_fresh[2]=week_fresh[2]+1
        elif 23<=i[2]<=29:
            week_fresh[3]=week_fresh[3]+1
    average=(week_fresh[0]+week_fresh[1]+week_fresh[2]+week_fresh[3])/4
    return average


def clean(id):
    data=rf.read_file(id)

    list_clean= []
    cleans= []

    cleans_boolean= data['State'].str.contains("주방 정리하기|전자렌지 청소하기|냉장고 정리하기").tolist()
    count=0
    for clean_bool in cleans_boolean:
        if clean_bool==True:
            cleans.append(int(count))
        count=count+1
    for i in cleans:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_clean:
            list_clean.append(date)
            
    week_clean=[0, 0, 0, 0]
    for i in list_clean:
        if 2<=i[2]<=8:
            week_clean[0]=week_clean[0]+1
        elif 9<=i[2]<=15:
            week_clean[1]=week_clean[1]+1
        elif 16<=i[2]<=22:
            week_clean[2]=week_clean[2]+1
        elif 23<=i[2]<=29:
            week_clean[3]=week_clean[3]+1
    
    average=(week_clean[0]+week_clean[1]+week_clean[2]+week_clean[3])/4
    return average

def wash(id):
    data=rf.read_file(id)

    list_washing= []
    washings= []

    washings_boolean= data['State'].str.contains("설거지|밥솥 정리").tolist()
    count=0
    for washing_bool in washings_boolean:
        if washing_bool==True:
            washings.append(int(count))
        count=count+1
    for i in washings:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_washing:
            list_washing.append(date)
    
    week_washing=[0, 0, 0, 0]
    for i in list_washing:
        if 2<=i[2]<=8:
            week_washing[0]=week_washing[0]+1
        elif 9<=i[2]<=15:
            week_washing[1]=week_washing[1]+1
        elif 16<=i[2]<=22:
            week_washing[2]=week_washing[2]+1
        elif 23<=i[2]<=29:
            week_washing[3]=week_washing[3]+1
    average=(week_washing[0]+week_washing[1]+week_washing[2]+week_washing[3])/4

    return average








