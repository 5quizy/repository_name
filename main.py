import json
import sqlite3
import requests

url = 'https://cat-fact.herokuapp.com/facts'
req = requests.get(url)
print(req.status_code)
print(req.headers)
print(req.text)
result = req.json()
with open('catfacts.json', 'w' ) as file:
    json.dump(result, file, indent=4)

connect = sqlite3.connect('cat_cats.sqlite')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE if not exists Cats

(id INTEGER PRIMARY KEY AUTOINCREMENT,
User VARCHAR(100),
Text VARCHAR(100)
);''')

for each in result:
    user_id = each['_id']
    t_text = each['text']
    cursor.execute('insert into Cats (user , text) VALUES(?,?)', (user_id, t_text))
    connect.commit()
connect.close()




