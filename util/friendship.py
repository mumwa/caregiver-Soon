import numpy as np
import pandas as pd
import datetime as dt
from dateutil.parser import parse
import math

user_data = pd.read_csv("util/user_profile.csv")
IDs = user_data["id"].values.tolist()

list_days = []
ID_to_index = []

num_msg1 = [] # 메시지1 출력 횟수
num_msg2 = []
num_msg3 = []

fre_resp1 = [] # 메시지1에 대한 응답 빈도
len_resp1 = [] # 메시지1에 대한 응답 평균 길이

fre_resp2 = []
len_resp2 = []

fre_resp3 = []
len_resp3 = []

num_conv = [] # 순이 대화 횟수
prop_conv = []

p_list = ['고마','고맙','감사','좋','응','그래','알았']
p_resp_prop = [] # 긍정적 등 특별 응답 

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
    
    msg1 = df[(df['Message_1'].notnull())]
    msg1 = msg1.drop(msg1[msg1['Message_1'] == '프로그램 메시지'].index)
    
    msg2 = msg1[msg1['Message_2'].notnull()]
    msg3 = msg2[msg2['Message_3'].notnull()]
    
    
    num_msg1.append(len(msg1))
    num_msg2.append(len(msg2))
    num_msg3.append(len(msg3))

    
    if len(msg1) != 0:
        fre_resp1.append(len(msg2)/len(msg1)) # 응답1의 빈도, 메시지 평균 길이
        sum_resp1 = 0
        for i in range(0,len(msg2)):
            sum_resp1 += len(msg2.iloc[i]['STT_1'])
        if len(msg2) != 0:
            sum_resp1 /= len(msg2)
        len_resp1.append(sum_resp1)
    else:
        fre_resp1.append(0)
        len_resp1.append(0)

    
    if len(msg2) != 0:
        fre_resp2.append(len(msg3)/len(msg2)) # 응답2의 빈도, 메시지 평균 길이  
        sum_resp2 = 0
        for i in range(0,len(msg3)):
            sum_resp2 += len(msg3.iloc[i]['STT_2'])
        if len(msg3) != 0:
            sum_resp2 /= len(msg3)
        len_resp2.append(sum_resp2)
    else:
        fre_resp2.append(0)
        len_resp2.append(0)        
    
    
    if len(msg3) != 0:
        tmp = msg3[msg3['STT_3'].notnull()] # 응답3의 빈도, 메시지 평균 길이
        fre_resp3.append(len(tmp)/len(msg3))
        sum_resp3 = 0
        for i in range(0,len(tmp)):
            sum_resp3 += len(tmp.iloc[i]['STT_3'])
        if len(tmp) != 0:
            sum_resp3 /= len(tmp)
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