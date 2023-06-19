from flask import Blueprint, render_template, request
import pickle
import sqlite3
import numpy as np
import os
import random

model_PATH = os.path.join(os.getcwd(), 'Apparel_app/views/model.pkl')

recom_bp = Blueprint('recommend', __name__, url_prefix='/recommend')
# 모델 불러오기
model = None
with open(model_PATH, 'rb') as file:
    model = pickle.load(file)
    
@recom_bp.route('/', methods=['POST','GET'])
def recommend():
    # 사용자 입력값 가져오기
    cup_size = request.form['cup_size'].lower()
    if bool(cup_size) == False:
        cup_size = 'a'
    try:
        hips = int(request.form['hips'])
    except:
        hips = 30
    try:
        height = int(request.form['height'])
    except:
        height = 155
    if request.form['fit'] == '선택':
        fit = '적당'
    else:
        fit = request.form['fit']
    # 사용자 입력값:변수 딕셔너리
    fit_dict = {
        '선택': None,
        '타이트':0,
        '적당':1,
        '루즈':2
    }
    cup_dict = {
        'aa':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11
    }
    size_dict = {0:44,1:55,2:66,3:77,4:88,5:99}
   
    # 사이즈 바꿔서 예측하기
    ##'cup_size', 'hips', 'height', 'item_size'
    # 예측값 반환하는 함수 정의
    def predict(hips, height): # 값을 입력하지 않으면 기본값
        size = 6
        for s in range(0,6):
            test = np.array([cup_dict[cup_size], hips, height, s]).reshape(1,-1)
            pred = model.predict(test)
            if pred == fit_dict[fit]: 
                if s < size:
                    size = s
        return size_dict[size]
    
    # 사용자 입력값으로 예측하기
    size = predict(hips, height)
    values = [cup_size, hips, height, size]
    
    return render_template('recommend.html',values=values), 200

@recom_bp.route('shop', methods=['POST','GET'])
def shop(): 
    cat_dict = {
            '신상품':'new',
            '상의':'tops',
            '바지':'bottoms',
            '스커트':'skirts',
            '원피스':'dresses',
            '아우터':'outwear',
            '세일':'sale'
        }
    cat = request.form['category']
    category = cat_dict[cat]
    # POST용 데이터
    # RDB에서 해당 카테고리 (이름, 이미지, 가격, 구매링크) 데이터 불러오기
    DBPATH = os.path.join(os.getcwd(), 'data/load/apparel_app.db')
    db = sqlite3.connect(DBPATH)
    cursor = db.cursor()
    cursor.execute('''
                   SELECT name, img, price, link
                   FROM item
                   WHERE category == ?;''', [category])
    try:
        item_info = random.sample(cursor.fetchall(),12)
    except:
        item_info = cursor.fetchall()
    units = len(item_info)
    return render_template('shop.html', item_info=item_info[:12], units=units, cat=cat, s=0), 200