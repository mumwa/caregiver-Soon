from util import social
from util import socialAverage


def social_score(id):
    my_score = social.social_me(int(id))
    all_score = socialAverage.all_social()
    if my_score<=(all_score*0.30):
        return "C"
    elif (all_score*0.30)<=my_score<=(all_score*1.30):
        return "B"
    else:
        return "A"
