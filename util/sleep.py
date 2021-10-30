#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import datetime as dt
from dateutil.parser import parse
import math

user_data = pd.read_csv("C:/Users/minjae/Desktop/lifelog/user_profile.csv")
IDs = user_data["id"].values.tolist()

list_avg_sleep = []
list_avg_sleep_nonzero = []
list_avg_nap = []
list_avg_nap_nonzero = []

list_days = []
list_num_sleep = []
list_num_wakeup = []
list_time_sleep = []

ID_to_index = []

for ID in IDs:
    ID_to_index.append(ID)
    if(ID > 30063):
        df = pd.read_csv("C:/Users/minjae/Desktop/lifelog/hs_g73_m08/hs_"+str(ID)+"_m08_0903_1356.csv",encoding="cp949")
    else:
        df = pd.read_csv("C:/Users/minjae/Desktop/lifelog/hs_g73_m08/hs_"+str(ID)+"_m08_0903_1355.csv",encoding="cp949")
    
    df["index"] = range(0,len(df))
    
    if len(df) <= 0: # 일수 계산
        list_days.append(0)
    else:  
        first_day = parse(df.iloc[0]['Time'])
        last_day = parse(df.iloc[len(df)-1]['Time'])
        list_days.append((last_day-first_day).days)
    

# 수면    
    s_w = df[(df['State'].str.contains("수면")) | (df['State'].str.contains("기상"))] # 낮잠 제외 수면 시간
    s_w = s_w.drop(s_w[s_w['State'].str.contains("낮잠")].index)
    
    sleep_time = []
    num_sleep = 0
    num_wakeup = 0
    time_to_sleep = []
    
    if len(s_w) <= 0:
        list_avg_sleep.append(0)
    else:
        if s_w.iloc[0]['State'] == "수면":
            num_sleep += 1
            time_to_sleep.append(parse(s_w.iloc[0]['Time']))
            flag = True
        else:
            num_wakeup += 1
            flag = False

        for i in range(1,len(s_w)):
            prev = s_w.iloc[i-1]['Time']
            next = s_w.iloc[i]['Time']
            if s_w.iloc[i]['State'] == "수면":
                num_sleep += 1
                time_to_sleep.append(parse(s_w.iloc[i]['Time']))
                if flag:
                    sleep = parse(prev)
                    tmp = df[(df['Time']) == prev].iloc[0]['index']
                    wake = parse(df[(df['index'] == tmp+1)].iloc[0]['Time'])
                    result = wake - sleep
                    flag = True
                else:
                    flag = True
                    continue
            else:
                num_wakeup += 1
                if flag:
                    sleep = parse(prev)
                    wake = parse(next)
                    result = wake - sleep
                else:
                    wake = parse(next)
                    tmp = df[(df['Time']) == next].iloc[0]['index']
                    wake = parse(df[(df['index'] == tmp-1)].iloc[0]['Time'])
                    result = wake - sleep

                flag = False

            if result.seconds < 1000:
                continue
            sleep_time.append(result.seconds)

        if len(sleep_time) == 0:
            list_avg_sleep.append(0)
            continue
        list_avg_sleep.append(np.mean(sleep_time))
        
    list_num_sleep.append(num_sleep) # '취침' 횟수
    list_num_wakeup.append(num_wakeup) # '기상' 횟수
    

    if len(time_to_sleep) == 0: # 취침 시각
        list_time_sleep.append(0)
    else:
        avg_h = 0
        avg_m = 0
        for i in range(0,len(time_to_sleep)):
            if time_to_sleep[i].hour <= 12:
                avg_h += time_to_sleep[i].hour + 24
            else:
                avg_h += time_to_sleep[i].hour
            avg_m += time_to_sleep[i].minute
        
        avg_h /= len(time_to_sleep)
        avg_m /= len(time_to_sleep)
        
        list_time_sleep.append(avg_h*60 + avg_m)

    nap_s_w = df[(df['State'].str.contains("낮잠"))] # 낮잠 시간
    nap_time = []

    if len(nap_s_w) <= 0: 
        list_avg_nap.append(0)
    else:
        if "낮잠자기" in nap_s_w.iloc[0]['State']:
            flag = True
        else:
            flag = False

        for i in range(1,len(nap_s_w)):
            prev = nap_s_w.iloc[i-1]['Time']
            next = nap_s_w.iloc[i]['Time']
            if "낮잠자기" in nap_s_w.iloc[i]['State']:
                if flag:
                    sleep = parse(prev)
                    tmp = df[(df['Time']) == prev].iloc[0]['index']
                    wake = parse(df[(df['index'] == tmp+1)].iloc[0]['Time'])
                    result = wake - sleep
                    flag = True
                else:
                    flag = True
                    continue
            else:

                if flag:
                    sleep = parse(prev)
                    wake = parse(next)
                    result = wake - sleep
                else:
                    wake = parse(next)
                    tmp = df[(df['Time']) == next].iloc[0]['index']
                    wake = parse(df[(df['index'] == tmp-1)].iloc[0]['Time'])
                    result = wake - sleep

                flag = False

            if result.seconds < 1000:
                continue
            nap_time.append(result.seconds)

        if len(nap_time) == 0:
            list_avg_nap.append(0)
            continue
        list_avg_nap.append(np.mean(nap_time))
    
        

for i in range(0,len(list_avg_sleep)):
    if list_avg_sleep[i] != 0:
        list_avg_sleep_nonzero.append(list_avg_sleep[i])
for i in range(0,len(list_avg_nap)):
    if list_avg_nap[i] != 0:
        list_avg_nap_nonzero.append(list_avg_nap[i])
        
# mean = np.mean(list_avg_sleep_nonzero) # 전체 수면시간 평균 (수면시간 관찰 x는 제외)
# std = np.std(list_avg_sleep_nonzero) # 전체 수면시간 표준편차

# list_avg_sleep # 전체 평균 수면시간 list (수면시간 관찰x나 0도 포함), 초 단위
# list_avg_nap # 전체 평균 낮잠시간 list, 초 단위
# list_num_sleep # '취침' 횟수 list
# list_num_wakeup # '기상' 쵯수 list
# list_days # 일수 list, 일 단위
# list_time_sleep # 평균 취침 시각 list, 분 단위


# 6~8시간이 적정량 => 5점, 그외에는 4점 
# 출처:https://m.health.chosun.com/svc/news_view.html?contid=2017032402755 (대한보건협회)
# 1시간 이상의 낮잠 => -1점
# 취침-기상 > 일수*0.1 => -1점 (기준 애매)
# 23시 이후 취침 => -1점
# 출처:https://health.chosun.com/site/data/html_dir/2019/06/14/2019061401739.html (멜라토닌 관련)

user_ID = 496
indx = ID_to_index.index(user_ID)
score = 5

fb_amount_of_sleep = 0 # 0 이하이면 수면량을 줄이도록, 0 이상이면 수면량을 늘리도록 피드백
fb_nap = 0 # 0 이상이면 낮잠량을 줄이도록 피드백
fb_day = 0 # 일정 기준량 이상 기상이 더 많으면 피드백,
fb_wakeup = 0 # fb_day 동안 fb_wakeup만큼의 수면장애
fb_gotobed = 0 # 23시 기준 취침 시간 피드백


if(list_avg_sleep[indx] < 6*3600): # 수면시간
    score -= 1
    fb_amount_of_sleep = math.ceil((6*3600 - list_avg_sleep[indx])/10)*10 # 10분 단위로 올림
elif(list_avg_sleep[indx] > 8*3600):
    score -= 1
    fb_amount_of_sleep = math.ceil((8*3600 - list_avg_sleep[indx])/10)*10 
    
if(list_avg_nap[indx] > 3600): # 낮잠시간
    score -= 1
    fb_nap = math.ceil((list_avg_nap[indx] - 3600)/10)*10

if((list_num_sleep[indx] - list_num_wakeup[indx]) > list_days[indx]*0.1): # 기상횟수
    score -= 1
    fb_day = list_days[indx]
    fb_wakeup = list_num_sleep[indx] - list_num_wakeup[indx] 
    
if(list_time_sleep[indx] > 60*23): # 취침시각
    score -= 1
    fb_gotobed = math.ceil((list_time_sleep[indx] - 60*23)/10)*10
    
print("Your score is " + str(score))
if(fb_amount_of_sleep > 0):
    print("You need to sleep more about " + str(fb_amount_of_sleep))
else:
    print("You need to sleep less about " + str(fb_amount_of_sleep))
if(fb_nap > 0):
    print("You need to abstain to nap about " + str(fb_nap))
if(fb_day != 0):
    print("You have" + str(fb_wakeup) + "sleep disorder" + str(fb_day) + "days")
if(fb_gotobed > 0):
    print("You need to go to bed early." + str(fb_gotobed) + " minutes earlier")


# In[ ]:




