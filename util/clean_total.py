#from util import cleanAverage
from util import read_file as rf
#import read_file as rf
import numpy as np
import pandas as pd

class Clean:
    user_ID = 0
    indx = 0

    data = 0
    user_data = 0
    IDs = 0

    clean_count = 0
    wash_count = 0
    fresh_count = 0

    avg_clean_count = 0
    avg_wash_count = 0
    avg_fresh_count = 0

    score_clean_count = "Wrong"
    score_wash_count = "Wrong"
    score_fresh_count = "Wrong"

    total_score = "Wrong"

    def fresh(self, id):
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

    def clean(self, id):
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

    def wash(self, id):
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

    def all_clean(self, IDs):
        all_clean=[]
        count=0
        total_average=0
        for id in IDs:
            value=self.clean(int(id))
            line=[id, value]
            all_clean.append(line)
            count=count+1
        for i in all_clean:
            total_average=total_average+i[1]
        return total_average/len(all_clean)

    def all_wash(self, IDs):
        all_wash=[]
        count=0
        total_average=0
        for id in IDs:
            value=self.wash(int(id))
            line=[id, value]
            all_wash.append(line)
            count=count+1
        for i in all_wash:
            total_average=total_average+i[1]
        return total_average/len(all_wash)

    def all_fresh(self, IDs):
        all_fresh=[]
        count=0
        total_average=0
        for id in IDs:
            value=self.fresh(int(id))
            line=[id, value]
            all_fresh.append(line)
            count=count+1#
        for i in all_fresh:
            total_average=total_average+i[1]
        return total_average/len(all_fresh)

    

    def __init__(self):
        self.user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
        self.IDs = self.user_data["id"].values.tolist()
        self.avg_clean_count = self.all_clean(self.IDs)
        self.avg_wash_count = self.all_wash(self.IDs)
        self.avg_fresh_count = self.all_fresh(self.IDs)


    def get_clean_grade(self, id):
        b=self.clean(int(id))
        a=self.clean(int(id))-self.avg_clean_count
        if (b<1):
            return "Alert"
        elif(a<0.25):
            return "C"
        elif(0.25<=a<=0.25):
            return "B"
        elif(a>0.25):
            return "A"
        else:
            return "Wrong"

    def get_wash_grade(self, id):
        b=self.wash(int(id))
        a=self.wash(int(id))-self.avg_wash_count
        if (b<3):
            return "Alert"
        elif(a<0.25):
            return "C"
        elif(0.25<=a<=0.25):
            return "B"
        elif(a>0.25):
            return "A"
        else:
            return "Wrong"
        
    def get_fresh_grade(self, id):
        b=self.fresh(int(id))
        a=self.fresh(int(id))-self.avg_fresh_count
        if (b<3):
            return "Alert"
        elif(a<0.25):
            return "C"
        elif(0.25<=a<=0.25):
            return "B"
        elif(a>0.25):
            return "A"
        else:
            return "Wrong"

    def get_grade(self, id):
        count_alert=0
        if(self.get_clean_grade(id)=="Alert"):
            count_alert=count_alert+1
        if(self.get_fresh_grade(id)=="Alert"):
            count_alert=count_alert+1
        if(self.get_wash_grade(id)=="Alert"):
            count_alert=count_alert+1

        if(count_alert<=1):
            return "A"
        elif(count_alert==2):
            return "B"
        elif(count_alert==3):
            return "C"
        else:
            return "Wrong"

