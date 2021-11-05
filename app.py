from flask import Flask, render_template, jsonify, request
# from bson.objectid import ObjectId
# 웹으로 작동하기 위한 라이브러리
from util import search as find
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

@app.route('/friendship')
def friendship():
    return render_template('friendship.html')

@app.route('/sleep')
def sleep():
    id = int(request.args["id"])
    sleep_result = total.Sleep(id)
    availableID = False
    if(find.search(id)):
        availableID = True
    return jsonify({'result': 'success', 'availableID': availableID, 'score_sleep': sleep_result.score_sleep,
    'fb_amount_of_sleep':sleep_result.fb_amount_of_sleep, 'fb_nap':sleep_result.fb_nap, 'fb_day':sleep_result.fb_day,
    'fb_wakeup':sleep_result.fb_wakeup, 'fb_gotobed':sleep_result.fb_gotobed
    })

@app.route('/meal')
def meal():
    id = int(request.args["id"])
    meal_result = total.Meal(id)
    availableID = False
    if(find.search(id)):
        availableID = True
    return jsonify({'result': 'success', 'availableID': availableID, 'score_meal': meal_result.score_meal,
    'fb_amount_of_meal':meal_result.fb_amount_of_meal, 'fb_num_bf':meal_result.fb_num_bf, 'fb_num_lun':meal_result.fb_num_lun,
    'fb_num_din':meal_result.fb_num_din, 'fb_time':meal_result.fb_time, 'fb_time_bf_early':meal_result.fb_time_bf_early,
    'fb_time_bf_late':meal_result.fb_time_bf_late, 'fb_time_lun_early':meal_result.fb_time_lun_early, 'fb_time_lun_late':meal_result.fb_time_lun_late,
    'fb_time_din_early':meal_result.fb_time_din_early, 'fb_time_din_late':meal_result.fb_time_din_late, 'fb_rg_bf':meal_result.fb_rg_bf,
    'fb_rg_lun':meal_result.fb_rg_lun, 'fb_rg_din':meal_result.fb_rg_din, 'fb_snack':meal_result.fb_snack, 'fb_n_snack':meal_result.fb_n_snack,
    'fb_fastfood':meal_result.fb_fastfood
    })

@app.route('/medicine')
def medicine():
    return render_template('medicine.html')

@app.route('/wash')
def wash():
    return render_template('wash.html')

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/categories')
def hobby():
    return render_template('categories.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)