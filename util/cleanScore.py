import cleanAverage
import clean

def get_clean_grade(id):
    b=clean.clean(int(id))
    a=clean.clean(int(id))-cleanAverage.all_clean()
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

def get_wash_grade(id):
    b=clean.wash(int(id))
    a=clean.wash(int(id))-cleanAverage.all_wash()
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
    
def get_fresh_grade(id):
    b=clean.fresh(int(id))
    a=clean.fresh(int(id))-cleanAverage.all_fresh()
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
