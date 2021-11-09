from flask import Flask, render_template, jsonify, request
# from bson.objectid import ObjectId
# 웹으로 작동하기 위한 라이브러리
from util import search as find

from util import clean
from util import cleanAverage
from util import cleanScore

from util import med
from util import medAverage
from util import medScore

from util import outside
from util import outsideScore

from util import social
from util import socialAverage
from util import socialScore

from util import emergency

from util import total

app = Flask(__name__)

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/find', methods=['GET'])
def find_id():
    id=int(request.args["id"])
    if(find.search(id)):
        ids=True
    else:
        ids=False
    return jsonify({'result': 'success', 'ids': ids})

@app.route('/hello', methods=['GET'])
def default():
    hello="hello"
    return jsonify({'result': 'success', 'hello': hello})

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/total_score')
def total_score():
    id=int(request.args["id"])
    sleep_score = total.Sleep(id)
    meal_score = total.Meal(id)
    wash_grade = cleanScore.get_grade(id)

    return jsonify()

@app.route('/alert')
def get_alert():
    id=int(request.args["id"])
    is_emergency=emergency.emergency(id)
    return jsonify({'result': 'success', 'emergency': is_emergency})

@app.route('/friendship')
def friendship_page():
    return render_template('friendship.html')

@app.route('/friends', methods=['GET'])
def get_friend():
    id=int(request.args["id"])
    friend_result = total.Friendship(id)
    # user_ID = 0
    # indx = 0
    # score_friendship 최종 점수 (friendship) 12점 만점에 df 점!ㅇ
    # fb_freq_resp 응답 빈도 00 / 15ㅇ
    # fb_len_resp 응답 길이 00 / 15ㅇ
    # fb_program = 0  ‘순이 대화’ 참여도 00 / 15
    # fb_keyword = False  특정 키워드 반응 

    # freq_resp1 = 0 첫번째 메시지는 00%로 답해주셨어요
    # freq_resp2 = 0 두번째 메시지는 00%로 답해주셨어요
    # freq_resp3 = 0 세번째 메시지는 00%로 답해주셨어요
    # len_resp = 0 총 몇자 답해주셨어요! 고마워요!
    # program = 0 00 회
    # prop_program = 0 nn%

    return jsonify({'num_msg1': friend_result.num_msg1, 'num_msg2': friend_result.num_msg2, 'num_msg3': friend_result.num_msg3, 'num_msg1_resp': friend_result.num_msg1_resp, 'num_msg2_resp': friend_result.num_msg2_resp, 'num_msg3_resp': friend_result.num_msg3_resp,  'result': 'success', 'score_sleep': friend_result.score_friendship, 'fb_freq_resp': friend_result.fb_freq_resp, 'fb_len_resp': friend_result.fb_len_resp, 'fb_program':friend_result.fb_program, 'fb_keyword':friend_result.fb_keyword, 'freq_resp1':friend_result.freq_resp1, 'freq_resp2':friend_result.freq_resp2, 'freq_resp3':friend_result.freq_resp3, 'len_resp':friend_result.len_resp, 'program':friend_result.program, 'prop_program':friend_result.prop_program,})

@app.route('/sleep')
def sleep():
    return render_template('sleep.html')

@app.route('/get_sleep', methods=['GET'])
def get_sleep():
    id = int(request.args["id"])
    sleep_result = total.Sleep(id)
    availableID = False
    if(find.search(id)):
        availableID = True
    return jsonify({'result': 'success', 'availableID': availableID, 'score_sleep': sleep_result.score_sleep, 'avg_sleep': sleep_result.avg_sleep, 'avg_gotobed': sleep_result.avg_gotobed,'fb_amount_of_sleep':sleep_result.fb_amount_of_sleep, 'fb_nap':sleep_result.fb_nap, 'fb_day':sleep_result.fb_day,'fb_wakeup':sleep_result.fb_wakeup, 'fb_gotobed':sleep_result.fb_gotobed})

@app.route('/meal')
def meal():
    return render_template('meal.html')

@app.route('/get_meal', methods=['GET'])
def get_meal():
    id = int(request.args["id"])
    meal_result = total.Meal(id)
    availableID = False
    if(find.search(id)):
        availableID = True
    return jsonify({'result': 'success', 'availableID': availableID, 'score_meal': meal_result.score_meal, 'avg_time_bf': meal_result.avg_time_bf, 'avg_time_lun': meal_result.avg_time_lun, 'avg_time_din': meal_result.avg_time_din, 'fb_amount_of_meal':meal_result.fb_amount_of_meal, 'fb_num_bf':meal_result.fb_num_bf, 'fb_num_lun':meal_result.fb_num_lun,'fb_num_din':meal_result.fb_num_din, 'fb_time':meal_result.fb_time, 'fb_time_bf_early':meal_result.fb_time_bf_early,'fb_time_bf_late':meal_result.fb_time_bf_late, 'fb_time_lun_early':meal_result.fb_time_lun_early, 'fb_time_lun_late':meal_result.fb_time_lun_late,'fb_time_din_early':meal_result.fb_time_din_early, 'fb_time_din_late':meal_result.fb_time_din_late, 'fb_rg_bf':meal_result.fb_rg_bf,'fb_rg_lun':meal_result.fb_rg_lun, 'fb_rg_din':meal_result.fb_rg_din, 'fb_snack':meal_result.fb_snack, 'fb_n_snack':meal_result.fb_n_snack,'fb_fastfood':meal_result.fb_fastfood})

@app.route('/medicine')
def medicine():
    return render_template('medicine.html')

@app.route('/wash')
def wash():
    return render_template('wash.html')

@app.route('/get_wash', methods=['GET'])
def get_wash():
    id=int(request.args["id"])

    get_clean_average=round(cleanAverage.all_clean(),2)
    get_wash_average=round(cleanAverage.all_wash(),2)
    get_fresh_average=round(cleanAverage.all_fresh(),2)

    grade=cleanScore.get_grade(id)

    get_clean_score=cleanScore.get_clean_grade(id)
    get_wash_score=cleanScore.get_wash_grade(id)
    get_fresh_score=cleanScore.get_fresh_grade(id)
    return jsonify({'result': 'success', 'clean': round(clean.clean(id),2), 'wash':round(clean.wash(id),2), 'fresh':round(clean.fresh(id),2), 'cleanAverage':get_clean_average, 'washAverage':get_wash_average, 'freshAverage':get_fresh_average, 'grade':grade, 'cleanGrade':get_clean_score, 'washGrade':get_wash_score,'freshGrade':get_fresh_score})

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/categories')
def hobby():
    return render_template('categories.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)