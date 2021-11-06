from util import social
from util import socialAverage


def social_score():
    if social.social_me(int(id))<=(socialAverage.all_social()*0.30):
        return "C"
    elif (socialAverage.all_social()*0.30)<=social.social_me(int(id))<=(socialAverage.all_social()*1.30):
        return "B"
    else:
        return "A"
