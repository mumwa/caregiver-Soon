from util import outside

def outsideScore(id):
    time = outside.recent_outside(id)
    if (time >= 15):
        return "A"
    else:
        return "B"
    