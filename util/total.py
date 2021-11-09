#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import datetime as dt
from dateutil.parser import parse
import math
from util import read_file as rf

user_data = pd.read_csv("util/user_profile.csv")
IDs = user_data["id"].values.tolist()
ID_to_index = []
list_days = []

# 수면
list_avg_sleep = []
list_avg_sleep_nonzero = []
list_avg_nap = []
list_avg_nap_nonzero = []
list_days = []
list_num_sleep = []
list_num_wakeup = []
list_time_sleep = []

# 식사
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

# friendship
num_msg1 = [] 
num_msg2 = []
num_msg3 = []

num_msg1_resp = []
num_msg2_resp = []
num_msg3_resp = []

fre_resp1 = [] 
len_resp1 = [] 

fre_resp2 = []
len_resp2 = []

fre_resp3 = []
len_resp3 = []

num_conv = []
prop_conv = []

p_list = ['고마','고맙','감사','좋','응','그래','알았']
p_resp_prop = [] 

for ID in IDs:
    ID_to_index.append(ID)
    df = rf.read_file(ID)
    df["index"] = range(0,len(df))
    
    # 일수 계산
    if len(df) <= 0: 
        list_days.append(0)
    else:  
        first_day = parse(df.iloc[0]['Time'])
        last_day = parse(df.iloc[len(df)-1]['Time'])
        list_days.append((last_day-first_day).days)
    
    # 수면
    s_w = df[(df['State'].str.contains("수면")) | (df['State'].str.contains("기상"))] 
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
                    if result.seconds >= 1000:
                        sleep_time.append(result.seconds)
                else:
                    flag = True
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
                if result.seconds >= 1000:
                    sleep_time.append(result.seconds)

        if len(sleep_time) == 0:
            list_avg_sleep.append(0)
        else:
            list_avg_sleep.append(np.mean(sleep_time))
        
    list_num_sleep.append(num_sleep) 
    list_num_wakeup.append(num_wakeup) 
    

    if len(time_to_sleep) == 0: 
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

    nap_s_w = df[(df['State'].str.contains("낮잠"))] 
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
                    if result.seconds >= 1000:
                        nap_time.append(result.seconds)
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

            if result.seconds >= 1000:
                nap_time.append(result.seconds)

        if len(nap_time) == 0:
            list_avg_nap.append(0)
        else:
            list_avg_nap.append(np.mean(nap_time))
    

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
        
    num_bf.append(b_num) 
    num_lun.append(l_num) 
    num_din.append(d_num) 
    time_bf.append(avg_bf) 
    time_lun.append(avg_lun) 
    time_din.append(avg_din) 
    std_bf.append(var_bf) 
    std_lun.append(var_lun) 
    std_din.append(var_din) 
    num_sn.append(s_num) 
    num_nsn.append(ns_num) 
    num_ff.append(ff_num) 
    num_total.append(total_num)

    

    # friendship
    msg1 = df[(df['Message_1'].notnull())]
    msg2 = df[(df['Message_2'].notnull())]
    msg3 = df[(df['Message_3'].notnull())]
    msg1_resp = df[(df['STT_1'].notnull())]
    msg2_resp = df[(df['STT_2'].notnull())]
    msg3_resp = df[(df['STT_3'].notnull())]
    msg1 = msg1.drop(msg1[msg1['Message_1'] == '프로그램 메시지'].index)


    num_msg1.append(len(msg1['Message_1']))
    num_msg2.append(len(msg2['Message_2']))
    num_msg3.append(len(msg3['Message_3']))
    num_msg1_resp.append(len(msg1_resp['STT_1']))
    num_msg2_resp.append(len(msg2_resp['STT_2']))
    num_msg3_resp.append(len(msg3_resp['STT_3']))


    if len(msg1) != 0:
        fre_resp1.append(len(msg1_resp)/len(msg1)*100) 
        sum_resp1 = 0
        for i in range(0,len(msg1_resp)):
            sum_resp1 += len(msg1_resp.iloc[i]['STT_1'])
        if len(msg1_resp) != 0:
            sum_resp1 /= len(msg1_resp)
        len_resp1.append(sum_resp1)
    else:
        fre_resp1.append(0)
        len_resp1.append(0)

    
    if len(msg2) != 0:
        fre_resp2.append(len(msg2_resp)/len(msg2)*100)   
        sum_resp2 = 0
        for i in range(0,len(msg2_resp)):
            sum_resp2 += len(msg2_resp.iloc[i]['STT_2'])
        if len(msg2_resp) != 0:
            sum_resp2 /= len(msg2_resp)
        len_resp2.append(sum_resp2)
    else:
        fre_resp2.append(0)
        len_resp2.append(0)        
    
    
    if len(msg3) != 0:
        fre_resp3.append(len(msg3_resp)/len(msg3)*100)
        sum_resp3 = 0
        for i in range(0,len(msg3_resp)):
            sum_resp3 += len(msg3_resp.iloc[i]['STT_3'])
        if len(msg3_resp) != 0:
            sum_resp3 /= len(msg3_resp)
        len_resp3.append(sum_resp3)
    else:
        fre_resp3.append(0)
        len_resp3.append(0)        
    
    
    pos_resp = 0
    
    for keyword in p_list:
        tmp = msg1[(msg1['STT_2'].astype(str).str.contains(keyword)) | (msg1['STT_3'].astype(str).str.contains(keyword))]
        pos_resp += len(tmp)
    
    
    if len(msg3) != 0:
        total_resp = len(msg2) + len(msg3) + len(tmp)
    else:
        total_resp = len(msg2) + len(msg3)
    
    if total_resp == 0:
        p_resp_prop.append(0)
    else:
        p_resp_prop.append(pos_resp/total_resp)
    
    total_program = df[(df['Act'].str.contains("프로그램 참여"))]
    conv = df[(df['State'].str.contains("대화"))]
    if len(conv) == 0:
        num_conv.append(0)
        prop_conv.append(0)
    else:
        num_conv.append(len(conv))
        prop_conv.append(len(total_program)/len(conv))

for i in range(0,len(list_avg_sleep)):
    if list_avg_sleep[i] != 0:
        list_avg_sleep_nonzero.append(list_avg_sleep[i])
for i in range(0,len(list_avg_nap)):
    if list_avg_nap[i] != 0:
        list_avg_nap_nonzero.append(list_avg_nap[i])
        
avg_fre_resp1 = np.mean(fre_resp1) # 메시지1에 대한 평균 응답 빈도
std_fre_resp1 = np.std(fre_resp1) # 메시지1에 대한 응답 빈도의 표준편차

avg_fre_resp2 = np.mean(fre_resp2) 
std_fre_resp2 = np.std(fre_resp2) 

avg_fre_resp3 = np.mean(fre_resp3) 
std_fre_resp3 = np.std(fre_resp3) 


avg_len_resp1 = np.mean(len_resp1) # 메시지1에 대한 응답 길이의 평균
std_len_resp1 = np.std(len_resp1) # 메시지1에 대한 응답 길이의 표준편차

avg_len_resp2 = np.mean(len_resp2) 
std_len_resp2 = np.std(len_resp2) 

avg_len_resp3 = np.mean(len_resp3) 
std_len_resp3 = np.std(len_resp3) 


avg_conv = np.mean(num_conv) # 순이 대화 횟수 평균
std_conv = np.std(num_conv) # 순이 대화 횟수 표준편차

avg_prop_conv = np.mean(prop_conv) # 순이 대화 횟수 평균
std_prop_conv = np.std(prop_conv) # 순이 대화 횟수 표준편차

avg_p_resp = np.mean(p_resp_prop) # 특정 키워드 평균



class Sleep:
    user_ID = 0
    indx = 0
    score_sleep = 5
    avg_sleep = 0
    avg_gotobed = 0
    fb_amount_of_sleep = 0 
    fb_nap = 0 
    fb_day = 0 
    fb_wakeup = 0 
    fb_gotobed = 0 

    def __init__(self, user_ID):
        self.userID = user_ID
        self.indx = ID_to_index.index(user_ID)
        self.avg_sleep = list_avg_sleep[self.indx]
        self.avg_gotobed = list_time_sleep[self.indx]
        
        if(list_avg_sleep[self.indx] < 6*3600): 
            self.score_sleep -= 1
            self.fb_amount_of_sleep = math.ceil((6*3600 - list_avg_sleep[self.indx])/10)*10 
        elif(list_avg_sleep[self.indx] > 8*3600):
            self.score_sleep -= 1
            self.fb_amount_of_sleep = math.ceil((8*3600 - list_avg_sleep[self.indx])/10)*10 
            
        if(list_avg_nap[self.indx] > 3600): 
            self.score_sleep -= 1
            self.fb_nap = math.ceil((list_avg_nap[self.indx] - 3600)/10)*10

        if((list_num_sleep[self.indx] - list_num_wakeup[self.indx]) > list_days[self.indx]*0.1): 
            self.score_sleep -= 1
            self.fb_day = list_days[self.indx]
            self.fb_wakeup = list_num_sleep[self.indx] - list_num_wakeup[self.indx] 
            
        if(list_time_sleep[self.indx] > 60*23): 
            self.score_sleep -= 1
            self.fb_gotobed = math.ceil((list_time_sleep[self.indx] - 60*23)/10)*10

class Meal:
    user_ID = 0
    indx = 0
    score_meal = 8
    avg_time_bf = 0
    avg_time_lun = 0
    avg_time_din = 0
    fb_amount_of_meal = False 
    fb_num_bf = False 
    fb_num_lun = False 
    fb_num_din = False 
    fb_time = 0 
    fb_time_bf_early = False 
    fb_time_bf_late = False 
    fb_time_lun_early = False
    fb_time_lun_late = False
    fb_time_din_early = False
    fb_time_din_late = False
    fb_rg_bf = False
    fb_rg_lun = False
    fb_rg_din = False
    fb_snack = 0 
    fb_n_snack = 0 
    fb_fastfood = 0 

    def __init__(self, user_ID):
        self.user_ID = user_ID
        self.indx = ID_to_index.index(user_ID)
        indx = self.indx

        self.avg_time_bf = time_bf[indx]
        self.avg_time_lun = time_lun[indx]
        self.avg_time_din = time_din[indx]

        if (num_bf[indx] + num_lun[indx] + num_din[indx])/3 < list_days[indx]/2:
            self.fb_amount_of_meal = True
            self.score_meal -= 1
        if num_bf[indx] < list_days[indx]/3:
            self.fb_num_bf = True
        if num_lun[indx] < list_days[indx]/3:
            self.fb_num_lun = True
        if num_din[indx] < list_days[indx]/3:
            self.fb_num_din = True
        if (self.fb_num_bf | self.fb_num_lun | self.fb_num_din):
            self.score_meal-= 1

        # 식사 시각 평가
        if time_bf[indx] < 360:
            self.fb_time_bf_early = True
            self.fb_time += 1
        elif time_bf[indx] > 480:
            self.fb_time_bf_late = True
            self.fb_time += 1
            
        if time_lun[indx] < 660:
            self.fb_time_lun_early = True
            self.fb_time += 1
        elif time_lun[indx] > 780:
            self.fb_time_lun_late = True    
            self.fb_time += 1
            
        if time_din[indx] < 1020:
            self.fb_time_din_early = True
            self.fb_time += 1
        elif time_din[indx] > 1140:
            self.fb_time_din_late = True    
            self.fb_time += 1
            
        if self.fb_time >= 3:
            self.score_meal -= 2
        elif self.fb_time > 0:
            self.score_meal -= 1

        # 식사 규칙성 평가
        if std_bf[indx] > 30:
            self.fb_rg_bf = True
        if std_lun[indx] > 30:
            self.fb_rg_lun = True
        if std_din[indx] > 30:
            self.fb_rg_din = True
        if (self.fb_rg_bf | self.fb_rg_lun | self.fb_rg_din):
            self.score_meal -= 1

        # 간식, 야식 평가
        if num_sn[indx] > list_days[indx]/3*2:
            self.fb_snack = num_sn[indx] - list_days[indx]/3*2
            self.score_meal -= 1
        if num_nsn[indx] > list_days[indx]/7:
            self.fb_n_snack = num_nsn[indx] - list_days[indx]/7
            self.score_meal -= 1

        # 간편식 평가
        if num_ff[indx] > list_days[indx]/2:
            self.fb_fastfood = num_ff[indx] - list_days[indx]/2
            self.score_meal -= 1

class Friendship:
    user_ID = 0
    indx = 0
    score_friendship = 0
    fb_freq_resp = 0
    fb_len_resp = 0
    fb_program = 0
    fb_keyword = False

    freq_resp1 = 0
    freq_resp2 = 0
    freq_resp3 = 0
    len_resp = 0
    program = 0
    prop_program = 0

    num_msg1 = 0
    num_msg2 = 0
    num_msg3 = 0

    num_msg1_resp = 0
    num_msg2_resp = 0
    num_msg3_resp = 0

    def __init__(self, user_ID):
        self.user_ID = user_ID
        self.indx = ID_to_index.index(user_ID)
        indx = self.indx

        
        self.num_msg1 = num_msg1[indx]
        self.num_msg2 = num_msg2[indx]
        self.num_msg3 = num_msg3[indx]

        self.num_msg1_resp = num_msg1_resp[indx]
        self.num_msg2_resp = num_msg2_resp[indx]
        self.num_msg3_resp = num_msg3_resp[indx]

        self.len_resp = (len_resp1[indx] + len_resp2[indx] + len_resp3[indx])/3

        self.program = num_conv[indx]
        self.prop_program = prop_conv[indx]

        if num_msg1_resp[indx] != 0:
            self.freq_resp1 = num_msg1_resp[indx]/num_msg1[indx]
        else:
            self.freq_resp1 = 0

        if num_msg2_resp[indx] != 0:  
            self.freq_resp2 = num_msg2_resp[indx]/num_msg2[indx]
        else:
            self.freq_resp2 = 0

        if num_msg3_resp[indx] != 0:
            self.freq_resp3 = num_msg3_resp[indx]/num_msg3[indx]
        else:
            self.freq_resp3 = 0

        if fre_resp1[indx] != 0:
            tmp_z1 = (fre_resp1[indx]-avg_fre_resp1)/std_fre_resp1
            self.fb_freq_resp += 2
            if tmp_z1 > 0:
                self.score_friendship += 0.5
                self.fb_freq_resp += 3
                if tmp_z1 > 0.53:
                    self.score_friendship += 0.5
                    self.fb_freq_resp += 5
                    
            if fre_resp2[indx] != 0:
                tmp_z2 = (fre_resp2[indx]-avg_fre_resp2)/std_fre_resp2
                self.fb_freq_resp += 2
                if tmp_z2 > 0:
                    self.score_friendship += 0.75
                    self.fb_freq_resp += 3
                    if tmp_z2 > 0.53:
                        self.score_friendship += 0.75
                        self.fb_freq_resp += 5
                        
                if fre_resp3[indx] != 0:
                    tmp_z3 = (fre_resp3[indx]-avg_fre_resp3)/std_fre_resp3
                    self.fb_freq_resp += 2
                    if tmp_z3 > 0:
                        self.score_friendship += 1
                        self.fb_freq_resp += 3
                        if tmp_z3 > 0.53:
                            self.score_friendship += 1 
                            self.fb_freq_resp += 5

                            
        if len_resp1[indx] != 0: 
            tmp_z1 = (len_resp1[indx]-avg_len_resp1)/std_len_resp1
            self.fb_len_resp += 2
            if tmp_z1 > 0:
                self.score_friendship += 0.5
                self.fb_len_resp += 3
                if tmp_z1 > 0.53:
                    self.score_friendship += 0.5
                    self.fb_len_resp += 5
                    
            if len_resp2[indx] != 0:
                tmp_z2 = (len_resp2[indx]-avg_len_resp2)/std_len_resp2
                self.fb_len_resp += 2
                if tmp_z2 > 0:
                    self.score_friendship += 0.75
                    self.fb_len_resp += 3
                    if tmp_z2 > 0.53:
                        self.score_friendship += 0.75
                        self.fb_len_resp += 5
                        
                if len_resp3[indx] != 0:
                    tmp_z3 = (len_resp3[indx]-avg_len_resp3)/std_len_resp3
                    self.fb_len_resp += 2
                    if tmp_z3 > 0:
                        self.score_friendship += 1
                        self.fb_len_resp += 3
                        if tmp_z3 > 0.53:
                            self.score_friendship += 1  
                            self.fb_len_resp += 5
                            
                            
        z1 = (num_conv[indx]-avg_conv)/std_conv 
        if z1 > 0:
            self.fb_program += 2
            self.score_friendship += 0.5
            if z1 > 0.53:
                self.fb_program += 2
                self.score_friendship += 0.25
                if z1 > 1.28:
                    self.fb_program += 2
                    self.score_friendship += 0.25

        z2 = (prop_conv[indx]-avg_prop_conv)/std_prop_conv 
        if z2 > 0:
            self.fb_program += 1
            self.score_friendship += 0.5
            if z2 > 0.53:
                self.fb_program += 0.5
                self.score_friendship += 0.25
                if z2 > 1.28:
                    self.fb_program += 0.5
                    self.score_friendship += 0.25
                    
                    
        if p_resp_prop[indx] > avg_p_resp: # 특정 키워드 평가
            self.score_friendship += 0.5
            self.fb_keyword = True
        if p_resp_prop[indx] >= 0.5:
            self.score_friendship += 0.5
            self.fb_keyword = True


# In[ ]:




