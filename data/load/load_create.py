import sqlite3

db = sqlite3.connect('./apparel_app.db')
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS USER;")
cur.execute("DROP TABLE IF EXISTS ITEM;")
cur.execute("DROP TABLE IF EXISTS REVIEW;")

cur.execute('''
            CREATE TABLE user(
                id VARCHAR(20) NOT NULL,
                cup_size VARCHAR(1),
                hips INTEGER,
                height REAL,
                PRIMARY KEY(id));''')

cur.execute('''
            CREATE TABLE item(
                id VARCHAR(20) NOT NULL,
                name VARCHAR(100),
                price VARCHAR(10),
                link VARCHAR(150),
                img VARCHAR(150),
                category VARCHAR(10),
                PRIMARY KEY(id));''')

cur.execute('''
            CREATE TABLE review(
                user_id VARCHAR(20) NOT NULL,
                item_id VARCHAR(20) NOT NULL,
                item_size INTEGER,
                length INTEGER,
                fit INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(id),
                FOREIGN KEY(item_id) REFERENCES item(id));''')
db.commit()
cur.close()
db.close()