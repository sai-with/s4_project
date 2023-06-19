### get: 사용자가 입력한 데이터 가져올 때
### post: 사용자에게 보여줄 데이터 보낼 때

import requests
from flask import Blueprint, render_template, redirect, url_for, request

main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def index():
  
  return render_template('index.html'), 200

# @main_bp.route('/post-to-recommend', methods=['POST'])
# def post_to_recommend(): 
#   # cup_size = request.form['cup_size'].lower()
#   # print(cup_size)
#   return redirect(url_for('recommend.recommend'))