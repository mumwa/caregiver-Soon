from util import read_file as rf
import numpy as np
import pandas as pd

class Medicine:
    user_ID = 0
    indx = 0

    data = 0
    user_data = 0
    IDs = 0

    def med(self, id):
        data=rf.read_file(id)

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
            med_time = round((hour+min+sec)/60)
            time_med.append(med_time)
        
        daily = []

        for i in range(len(list_calendar)):
            daily.append([])
            per_day = list_med.count(list_calendar[i])
            for j in range(per_day):
                daily[i].append(time_med[i+j])

        #calculate daily AVERAGE per day
        dailyAverage  = []
        avg=0
        for i in range(len(daily)):
            avg = daily[i][len(daily[i])-1] - daily[i][0]
            if(len(daily[i])==0):
                avg=0
            else:
                avg = avg/len(daily[i])
            dailyAverage.append(avg)

        return dailyAverage

    #medicine I recently took
    def recent_med(self, id):
        list = self.med(int(id))
        length = len(list)

        if(length>1):
            return int(list[length-1])
        else:
            return 0

    user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
    IDs = user_data["id"].values.tolist()

    #My All Medicine Lists
    def all_med(self, id):
        avg_div = 0
        my_list = self.med(int(id))
        if(len(my_list)==0):
            return 0
        else:
            for i in range(len(my_list)):
                avg_div = avg_div + my_list[i]
            avg = round(avg_div/len(my_list))
            return avg

    def __init__(self):
        self.user_data = pd.read_csv("util/user_profile.csv", encoding="cp949")
        self.IDs = self.user_data["id"].values.tolist()

    #calculate your grade
    def get_med_grade(self, id):
        today = self.recent_med(int(id))
        normal = self.all_med(int(id))

        if(normal==0):
            return "X"
        #if same, great
        #if more, need to be tightened
        #if less, need to be less
        if(today==normal):
            return "A"
        elif(today>normal):
            return "C"
        else:
            return "B"
