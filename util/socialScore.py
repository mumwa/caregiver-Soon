import social
import socialAverage


def social_score():
    if social_me(int(id))<=(socialAverage.all_social()*0.30):
        return "C"
    elif (social_me(int(id))>=(socialAverage.all_social()*0.30) && social_me()<=(socialAverage.all_social()*1.30)):
        return "B"
    else:
        return "A"
