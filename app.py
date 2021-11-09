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

@app.route('/friends', methods=['GET'])
def get_friend():
    #id=int(request.args["id"])
    hello="허허"
    return jsonify({'result': 'success', 'hello': hello})

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/alert')
def get_alert():
    id=int(request.args["id"])
    is_emergency=emergency.emergency(id)
    return jsonify({'result': 'success', 'emergency': is_emergency})

@app.route('/friendship')
def friendship_page():
    return render_template('friendship.html')

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

@app.route('/get_medicine')
def get_medicine():
    id = int(request.args["id"])

    recent_med = med.recent_med(id)
    grade = medScore.get_med_grade(id)
    average = medAverage.all_med(id)
    return jsonify({'result': 'success', 'grade': grade, 'recent_med' : recent_med, 'average' : average })


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

@app.route('/get_activity', methods=['GET'])
def get_activity():
    id=int(request.args["id"])
    time = outside.recent_outside(id)
    grade = outsideScore.outsideScore(id)
    mine = social.social_me(id)
    average = socialAverage.all_social()
    socialGrade = socialScore.social_score(id)
    return jsonify({'result':'success', 'time': time, 'grade' : grade, 'mine': mine, 'average':average, 'socialGrade':socialGrade})

@app.route('/categories')
def hobby():
    return render_template('categories.html')

@app.route('/get_categories')
def get_categories():
    id=int(request.args["id"])
    meal_grade = total.Meal(id)
    sleep_grade = total.Sleep(id)
    med_grade = medScore.get_med_grade(id)
    wash_grade=cleanScore.get_grade(id)
    activity_grade = outsideScore.outsideScore(id)
    return jsonify({'result':'success', 'meal':meal_grade, 'sleep':sleep_grade,'med': med_grade, 'wash':wash_grade, 'activity':activity_grade})

#for commit
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)