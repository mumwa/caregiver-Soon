#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import datetime as dt
from dateutil.parser import parse
import math

user_data = pd.read_csv("util/user_profile.csv", encoding="euc-kr")
IDs = user_data["id"].values.tolist()

list_days = []

num_total = []

num_bf = []
num_lun = []
num_din = []

time_bf = []
time_lun = []
time_din = []

std_bf = []
std_lun = []
std_din = []

num_sn = []
num_nsn = []
num_ff = []

ID_to_index = []

for ID in IDs:
    ID_to_index.append(ID)
    if(ID > 30063):
        df = pd.read_csv("../data/hs_"+str(ID)+"_m08_0903_1356.csv",encoding="cp949")
    else:
        df = pd.read_csv("../data/hs_"+str(ID)+"_m08_0903_1355.csv",encoding="cp949")
    
    df["index"] = range(0,len(df))
    
    if len(df) <= 0: # 일수 계산
        list_days.append(0)
    else:  
        first_day = parse(df.iloc[0]['Time'])
        last_day = parse(df.iloc[len(df)-1]['Time'])
        list_days.append((last_day-first_day).days)
    

    # 식사    
    b_df = df[(df['Act'].str.contains("아침식사"))] 
    l_df = df[(df['Act'].str.contains("점심식사"))] 
    d_df = df[(df['Act'].str.contains("저녁식사"))] 
    s_df = df[(df['Act'].str.contains("간식"))]
    ns_df = df[(df['Act'].str.contains("야식"))]
    ff_df = df[(df['State'].str.contains("간편식"))]
    
    food_out = df[(df['State'].str.contains("음식 꺼내기"))] 
    
    b_num = len(b_df)
    l_num = len(l_df)
    d_num = len(d_df)
    s_num = len(s_df)
    ns_num = len(ns_df)
    ff_num = len(ff_df)
    total_num = len(food_out)
    
    # 아침식사 시간
    if b_num != 0:
        list_breakfast = []
        for i in range(0,b_num):
            tmp = parse(b_df.iloc[i]['Time'])
            list_breakfast.append(tmp.hour*60 + tmp.minute)
        avg_bf = np.mean(list_breakfast)
        var_bf = np.std(list_breakfast)
    else:
        avg_bf = 0
        var_bf = 0
    
    # 점심식사 시간
    if l_num != 0:
        list_lunch = []
        for i in range(0,l_num):
            tmp = parse(l_df.iloc[i]['Time'])
            list_lunch.append(tmp.hour*60 + tmp.minute)
        avg_lun = np.mean(list_lunch)
        var_lun = np.std(list_lunch)
    else:
        avg_lun = 0
        var_lun = 0
        
    # 저녁식사 시간
    if d_num != 0:
        list_dinner = []
        for i in range(0,d_num):
            tmp = parse(d_df.iloc[i]['Time'])
            list_dinner.append(tmp.hour*60 + tmp.minute)
        avg_din = np.mean(list_dinner)
        var_din = np.std(list_dinner)
    else:
        avg_din= 0
        var_din = 0
        
    num_bf.append(b_num) # 아침식사 횟수
    num_lun.append(l_num) # 점심식사 횟수
    num_din.append(d_num) # 저녁식사 횟수
    
    time_bf.append(avg_bf) # 평균 아침식사 시간 (분으로 나타냄)
    time_lun.append(avg_lun) # 평균 점심식사 시간
    time_din.append(avg_din) # 평균 저녁식사 시간
    
    std_bf.append(var_bf) # 아침식사 평균편차
    std_lun.append(var_lun) # 점심식사 평균편차
    std_din.append(var_din) # 저녁식사 평균편차
    
    num_sn.append(s_num) # 간식 횟수
    num_nsn.append(ns_num) # 야식 횟수
    num_ff.append(ff_num) # 간편식 횟수
    
    num_total.append(total_num)
    
# 밑부분은 ID가 주어졌을 때
user_ID = 496
indx = ID_to_index.index(user_ID)
score = 10

fb_amount_of_meal = False # 식사 양
fb_num_bf = False # 아침식사 양
fb_num_lun = False # 점심식사 양
fb_num_din = False # 저녁식사 양

fb_time = 0 
fb_time_bf_early = False # 너무 이른 아침식사 피드백
fb_time_bf_late = False # 너무 늦은 아침식사 피드백 (이하 동일)
fb_time_lun_early = False
fb_time_lun_late = False
fb_time_din_early = False
fb_time_din_late = False

fb_rg_bf = False # 아침식사 규칙성 피드백
fb_rg_lun = False
fb_rg_din = False

fb_snack = 0 # 간식 빈도 피드백
fb_n_snack = 0 # 야식 빈도 피드백
fb_fastfood = 0 # 간편식 피드백

# 식사 횟수 평가
if (num_bf[indx] + num_lun[indx] + num_din[indx])/3 < list_days[indx]/2:
    fb_amount_of_meal = True
    score -= 1
if num_bf[indx] < list_days[indx]/3:
    fb_num_bf = True
if num_lun[indx] < list_days[indx]/3:
    fb_num_lun = True
if num_din[indx] < list_days[indx]/3:
    fb_num_din = True
if (fb_num_bf | fb_num_lun | fb_num_din):
    score -= 1

# 식사 시각 평가
if time_bf[indx] < 360:
    fb_time_bf_early = True
    fb_time += 1
elif time_bf[indx] > 480:
    fb_time_bf_late = True
    fb_time += 1
    
if time_lun[indx] < 690:
    fb_time_lun_early = True
    fb_time += 1
elif time_lun[indx] > 780:
    fb_time_lun_late = True    
    fb_time += 1
    
if time_din[indx] < 930:
    fb_time_din_early = True
    fb_time += 1
elif time_din[indx] > 1170:
    fb_time_din_late = True    
    fb_time += 1
    
if fb_time >= 3:
    score -= 2
elif fb_time > 0:
    score -= 1

# 식사 규칙성 평가
if std_bf[indx] > 30:
    fb_rg_bf = True
if std_lun[indx] > 30:
    fb_rg_lun = True
if std_din[indx] > 30:
    fb_rg_din = True
if (fb_rg_bf | fb_rg_lun | fb_rg_din):
    score -= 1

# 간식, 야식 평가
if num_sn[indx] > list_days[indx]/3*2:
    fb_snack = num_ns[indx] - list_days[indx]/3*2
    score -= 1
if num_nsn[indx] > list_days[indx]/5:
    fb_n_snack = num_nsn[indx] - list_days[indx]/5
    score -= 1

# 간편식 평가
if num_ff[indx] > list_days[indx]/2:
    fb_fastfood = num_ff[indx] - list_days[indx]/2
    score -= 1

    


# In[ ]:




