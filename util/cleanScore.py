import cleanAverage
import clean

def get_clean_grade(id):
    a=clean.clean(int(id))-cleanAverage.all_clean()
    if(a<0):
        return "C"
    elif(a==0):
        return "B"
    elif(a>0):
        return "A"
    else:
        return "Wrong"

def get_wash_grade(id):
    a=clean.wash(int(id))-cleanAverage.all_wash()
    if(a<0):
        return "C"
    elif(a==0):
        return "B"
    elif(a>0):
        return "A"
    else:
        return "Wrong"
    
def get_fresh_grade(id):
    a=clean.fresh(int(id))-cleanAverage.all_fresh()
    if(a<0):
        return "C"
    elif(a==0):
        return "B"
    elif(a>0):
        return "A"
    else:
        return "Wrong"
