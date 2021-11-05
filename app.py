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
#from util import socialScore

from util import meal

from util import friendship

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

@app.route('/friendship')
def friendship_page():
    return render_template('friendship.html')

@app.route('/sleep')
def sleep():
    return render_template('sleep.html')

@app.route('/meal')
def meal_page():
    return render_template('meal.html')

@app.route('/medicine')
def medicine():
    return render_template('medicine.html')

@app.route('/wash')
def wash():
    return render_template('wash.html')

@app.route('/get_wash', methods=['GET'])
def get_wash():
    id=int(request.args["id"])
    return jsonify({'result': 'success', 'clean': clean.clean(id), 'wash':clean.wash(id), 'fresh':clean.fresh(id), })

@app.route('/activity')
def activity():
    return render_template('activity.html')

@app.route('/categories')
def hobby():
    return render_template('categories.html')

#for commit
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)