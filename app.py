from flask import Flask, render_template, jsonify, request
# from bson.objectid import ObjectId
# 웹으로 작동하기 위한 라이브러리
from util import search as find
from util.med import med
from util.medAverage import all_med
from util.medScore import get_med_grade, print_message
from util.socialScore import social_score


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
    return render_template('sleep.html')

@app.route('/meal')
def meal():
    return render_template('meal.html')

@app.route('/medicine')
def medicine(id):
    score = get_med_grade(id)
    time = med(id)
    totalAverage = all_med(id)
    message = print_message(id)
    return render_template('medicine.html', template_score = score, template_time = time, template_totalAverage = totalAverage, template_msg = message)

@app.route('/wash')
def wash():
    return render_template('wash.html')

@app.route('/activity')
def activity():
    score = social_score()

    return render_template('activity.html', template_score = score)

@app.route('/categories')
def hobby():
    return render_template('categories.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)