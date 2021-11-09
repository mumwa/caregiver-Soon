from util import socialAverage
import numpy as np
import pandas as pd
from util import read_file

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

    if(len(list_social)==0):
        return 0
    else:
        average=len(programs) / len(list_social)
        return average
