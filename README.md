# caregiver-Soon
A care program for the elderly living alone that analyzes and provides sensor data installed in the house.

### **프로그램 설명**

2021-2 연세대학교 컴퓨터 과학과 프로그래밍 언어 구조론 팀 프로젝트이다. 독거 노인 분들의 생활에서 센서로 수집한 라이프로그 데이터를 가공하여 웹으로 표시하였다. python과 javascript를 사용하였다.

### **사용 라이브러리/프레임워크**

flask, numpy, pandas

### **실행 방법**

flask, numpy, pandas가 포함된 가상환경을 실행시킨 후 최상위 디렉토리(caregiver-Soon)에서 python app.py(혹은 파이썬 버전에 따라 python3 app.py)를 실행한다.

### **파일 구조**

**-data**: 라이프로그 csv 파일

**-util**: data들을 가공하는 python 모듈. 주로 점수값을 return한다. numpy, pandas 라이브러리 사용

**-static**: 로딩이 오래 걸리고 변경이 잘 일어나지 않는 이미지 파일/css 파일이 들어간다. flask가 캐시 파일로 저장되도록 한다.

.**-templates**: javascript 코드가 포함된 html 파일. static의 파일들과 연결. ajax로 app.py에 요청을 보내 값을 받아오고 jquery를 사용하여 화면에 값을 반영한다.

**app.py**: flask를 사용하여 요청을 받고 util 모듈들을 사용하여 값을 return하는 파일. flask 모듈 render_template, jsonify, request 사용한다. render_template으로 html 파일을 띄운다. jsonify, request로 json 형식으로 요청을 주고 받는다.

### **세부 설명**

**static**

style.css 공통 스타일 양식/외 기타 이미지

**templates**

@app.route(‘/‘)->search.html 아이디 확인

@app.route(‘/home‘)->main.html 메인 점수 표기

@app.route('/categories’)->categories.html 카테고리별 메인 점수 표기, 각 세부 페이지로 이동

@app.route(‘/friendship‘)->friendship.html 친밀도 표기

@app.route(‘/sleep‘)->sleep.html 취침시간 표기

@app.route(‘/meal‘)->meal.html 식사시간 표기@app.route(‘/medicine‘)->medicine.html 투약시간 표기

@app.route(‘/wash‘)->wash.html 청결도 표기

@app.route(‘/activity‘)->activity.html 외부활동성 표기

**util**

-read_file.py: 매개변수로 아이디를 받아 csv파일 링크를 리턴(pandas)

-total.py: Friendship, Meal, Sleep class. init시 평균/ 전체 점수를 저장 후 변수에 저장. id를 받아 점수들을 변수에 저장(numpy, pandas, datetime,dateutil)

-clean_total.py: Clean class. init 시전체 평균을 변수에 저장. 메소드들에서 매개변수로 id를 받아 점수와 주간 평균 횟수를 return(numpy, pandas)

-med_total.py: Medicine class. init 시전체 평균을 변수에 저장. 메소드들에서 매개변수로 id를 받아 점수와 주간 평균 횟수를 return(numpy, pandas)

-act_total.py: Activity class. init 시전체 평균을 변수에 저장. 메소드들에서 매개변수로 id를 받아 점수와 주간 평균 횟수를 return(numpy, pandas)

-emergency.py:id를 매개변수로 받아 하루 이상 외출 없이 부동이 이어질 경우 emergency 여부를 boolean으로 return(numpy, pandas)

-score.py: id를 매개변수로 아이디를 받아 csv파일 링크를 string으로 리턴(pandas)
