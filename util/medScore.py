import medAverage
import med

def get_med_grade(id):
    a=med.med(int(id))-medAverage.all_med(id)
    if(a>0):
        return "Too much"
    elif(a==0):
        return "B"
    else:
        return "Take your medicine regularly."