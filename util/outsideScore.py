from util import outside

def outsideScore(id):
    average = outside.outside_average(id)
    if (average >= 7):
        return "A"
    elif(0<=average<=7):
        return "B"
    else:
        return "C"