import sqlite3
import pandas as pd
import warnings
import os
warnings.filterwarnings(action='ignore')

# 데이터 불러오기
CSVPATH_1 = os.path.join(os.getcwd(),'processed_df.csv')
CSVPATH_2 = os.path.join(os.getcwd(),'item_info.csv')
data = pd.read_csv(CSVPATH_1)

columns =['item_id','category','user_id','cup_size','hips','height','length','fit']

# db 연결하기
DBPATH = './apparel_app.db'
db = sqlite3.connect(DBPATH)
cur = db.cursor()
# 데이터 입력
## item_id 중복제거 후 입력
item = pd.read_csv(CSVPATH_2)
item['id'] = list(set(data['item_id'])) # id 열 추가
item = item[['id', 'item_name', 'item_price', 'item_link', 'item_img', 'category']]

for row in list(item.itertuples(index=False, name=None)):
    cur.execute('''
                INSERT INTO item VALUES (?,?,?,?,?,?);''', row)
## user_id 중복제거 후 입력    
user = data[columns[2:6]]
user_dup = user.loc[user.user_id.duplicated()==True]
user.drop(user_dup.index, axis=0, inplace=True)

for row in list(user.itertuples(index=False, name=None)):
    cur.execute('''
                INSERT INTO user VALUES (?,?,?,?);''', row)

review = data[['user_id', 'item_id', 'item_size','length', 'fit']]
for row in list(review.itertuples(index=False, name=None)):
    cur.execute('''
                INSERT INTO review VALUES (?,?,?,?,?);''', row)
# 커밋 후 연결해제    
db.commit()
cur.close()
db.close()

print(len(data))