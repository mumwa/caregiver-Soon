from util import total
from util import medScore
from util import cleanScore
from util import outsideScore
from util import medScore
import math
import numpy as np

list_score = []
avg_score = 0
std_score = 0

for ID in total.IDs:
    sum = 0
    sleep_score = total.Sleep(ID).score_sleep
    meal_score = total.Meal(ID).score_meal
    friendship_score = total.Friendship(ID).score_friendship
    wash_grade = cleanScore.get_grade(ID)
    medicine_grade = medScore.get_med_grade(ID)
    activity_grade = outsideScore.outsideScore(ID)

    if medicine_grade == "X":
        if sleep_score <= 1:
            sum += 5
        elif sleep_score <= 3:
            sum += 10
        elif sleep_score <= 5:
            sum += 20
        else:
            sum += 5

        if meal_score <= 2:
            sum += 5
        elif meal_score <= 5:
            sum += 10
        elif meal_score <= 8:
            sum += 20
        else:
            sum += 5

        if friendship_score < 3:
            sum += 5
        elif friendship_score <= 7:
            sum += 10
        else:
            sum += 20

        if wash_grade == "C":
            sum += 5
        elif wash_grade == "B":
            sum += 10
        elif wash_grade == "A":
            sum += 20
        else:
            sum += 5

        if activity_grade == "C":
            sum += 5
        elif activity_grade == "B":
            sum += 10
        elif activity_grade == "A":
            sum += 20
        else:
            sum += 5
    else:
        if sleep_score <= 1:
            sum += 4
        elif sleep_score <= 3:
            sum += 8
        elif sleep_score <= 5:
            sum += 16
        else:
            sum += 4

        if meal_score <= 2:
            sum += 4
        elif meal_score <= 5:
            sum += 8
        elif meal_score <= 8:
            sum += 16
        else:
            sum += 4

        if friendship_score < 3:
            sum += 4
        elif friendship_score <= 7:
            sum += 8
        else:
            sum += 16

        if wash_grade == "C":
            sum += 4
        elif wash_grade == "B":
            sum += 8
        elif wash_grade == "A":
            sum += 16
        else:
            sum += 4

        if medicine_grade == "C":
            sum += 4
        elif medicine_grade == "B":
            sum += 8
        elif medicine_grade == "A":
            sum += 16
        else:
            sum += 4

        if activity_grade == "C":
            sum += 4
        elif activity_grade == "B":
            sum += 8
        elif activity_grade == "A":
            sum += 16
        else:
            sum += 4
        
        sum = (math.floor(sum/5)+1)*5
    
    list_score.append(sum)

avg_score = np.mean(list_score)
std_score = np.std(list_score)

print(list_score)
print(len(list_score))

def returnScore(ID):
    return list_score[total.ID_to_index(ID)]