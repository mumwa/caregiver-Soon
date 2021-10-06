from flask import Flask, render_template, jsonify, request
# from bson.objectid import ObjectId
# 웹으로 작동하기 위한 라이브러리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 데이터 가져오는 라이브러리

#민재님
data=pd.read_csv("data/hs_30076_m08_0903_1356.csv", index_col=0, encoding="euc-kr")

#예림님


#효정님



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def default():
    hello="hello"
    return jsonify({'result': 'success', 'hello': hello})

@app.route('/search')
def search():
    return render_template('search.html')

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

@app.route('/hobby')
def hobby():
    return render_template('hobby.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)