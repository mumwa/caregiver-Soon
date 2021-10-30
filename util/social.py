import socialAverage
import numpy as np
import pandas as pd

def read_file(id):
    if(id > 30063):
        file="../data/hs_"+str(id)+"_m08_0903_1356.csv"
    else:
        file="../data/hs_"+str(id)+"_m08_0903_1355.csv"
    data=pd.read_csv(file, encoding="cp949")
    return data


def social_me(id):
    data=read_file(id)

    list_social= []
    socials= []

    programs= data['Act'].str.contains("프로그램 참여").tolist()
    count=0
    for prog in programs:
        if prog==True:
            socials.append(int(count))
        count=count+1
    for i in socials:
        mass=data.iloc[i]['Time'].split(' ')
        date=mass[0].split('-')
        year=date[0]
        date[0]=int(year[1:5])
        date[1]=int(date[1])
        date[2]=int(date[2])
        if date not in list_social:
            list_social.append(date)

    average=len(programs) / len(list_social)
    return average
