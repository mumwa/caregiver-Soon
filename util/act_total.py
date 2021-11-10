from util import outside
from util import outsideScore
from util import social
from util import socialAverage
from util import socialScore

from util import read_file as rf

import numpy as np
import pandas as pd



class Activity:
    user_ID = 0
    indx = 0

    data = 0
    user_data = 0
    IDs = 0

    avg_social_count = 0

    #Count how many times I went outside
    def outside(self, id):
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

    def outside_average(self, id):
        weekly = self.outside(id)
        average=(weekly[0]+weekly[1]+weekly[2]+weekly[3])/4

        return average


    def outsideScore(self, id):
        average = self.outside.outside_average(id)
        if (average >= 7):
            return "A"
        elif(0<=average<=7):
            return "B"
        else:
            return "C"

    def social_me(self, id):
        data=rf.read_file(id)

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
            return round(average)

    user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
    IDs = user_data["id"].values.tolist()

    def all_social(self, IDs):
        #All people avg_of "social_me"
        all_social=[]
        count=0
        total_average=0
        for id in IDs:
            value=self.social.social_me(int(id))
            line=[id, value]
            all_social.append(line)
            count=count+1
        for i in all_social:
            total_average=total_average + i[1]
        return int(total_average/len(all_social))

    def __init__(self):
        self.user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
        self.IDs = self.user_data["id"].values.tolist()
        self.avg_social_count = self.all_social(self.IDs)


    def social_score(self, id):
        my_score = self.social.social_me(int(id))
        if my_score<=(self.avg_social_count*0.30):
            return "C"
        elif (self.avg_social_count*0.30)<=my_score<=(self.avg_social_count*1.30):
            return "B"
        else:
            return "A"