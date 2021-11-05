import pandas as pd

def read_file(id):
    if(id > 30063):
        file="../data/hs_"+str(id)+"_m08_0903_1356.csv"
    else:
        file="../data/hs_"+str(id)+"_m08_0903_1355.csv"
    data=pd.read_csv(file, encoding="euc-kr")
    return data