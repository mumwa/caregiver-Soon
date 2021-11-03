from flask import Flask, render_template, jsonify, request
# from bson.objectid import ObjectId
# 웹으로 작동하기 위한 라이브러리
from util import search as find


app = Flask(__name__)

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/hello', methods=['GET'])
def default():
    hello="hello"
    return jsonify({'result': 'success', 'hello': hello})

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/find', methods=['GET'])
def find_id():
    id=int(request.args["id"])
    ids="what"
    if(find.search(id)):
        ids=True
    else:
        ids=False
    return jsonify({'result': 'success', 'ids': ids})

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