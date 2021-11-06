import medAverage
import med

#med(id)는 일일 복용 시간 간격을 계산함
#medAverage 는 일반적인 개인 복용 시간 간격을 계산함

def get_med_grade(id):
    today = med.recent_med(int(id))
    normal = medAverage.all_med(int(id))

    if(normal==0):
        return "No Data"
#if same, great
#if more, need to be tightened
#if less, need to be less
    if(today==normal):
        return "A"
    elif(today>normal):
        return "C"
    else:
        return "B"


def print_message(id):
    score = get_med_grade(int(id))
    if(score=="A"):
        "약도 잘 챙겨주시네요! 순이가 박수 드릴게요"
    elif(score=="B"):
        "약을 잘 챙겨드시는 건 좋지만, 복용간격이 너무 가까우면 부작용이 있으니 주의해주세요."
    elif(score=="C"):
        "아이코, 깜빡하셨나보네요! 약을 눈에 잘 보이는 곳에 두는 것이 어떨까요?"
    else:
        "약을 규칙적으로 챙겨드시면 좋답니다. 순이와 함께 건강한 생활 시작해보시는 거 어때요?"