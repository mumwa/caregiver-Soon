import med
import numpy as np
import pandas as pd

user_data = pd.read_csv("user_profile.csv", encoding="euc-kr")
IDs = user_data["id"].values.tolist()


def all_med(id):
    data=med.read_file(id)

    days_med= []
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
        if date not in days_med:
            days_med.append(date)

    numbers=0
    for i in len(med(id)):
        numbers += med(id)[i]
    daily_med = numbers/len(days_med)

    return daily_med