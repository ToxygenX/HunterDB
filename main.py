import os
import zipfile
import sqlite3
from flask import Flask
from flask import request

app = Flask(__name__)

os.system("wget https://eu-amsterdam.rapidleech.gq/files/data.zip")

with zipfile.ZipFile("data.zip","r") as zf:
    zf.extractall()
for item in os.listdir(path='.'):
    print("Extracted - Database to Server")

def username_s(username):
    con = sqlite3.connect('data.db')
    mycursor = con.cursor()
    myresult = mycursor.execute("SELECT * from users WHERE username ='{}' LIMIT 1".format(username))  
    a = []
    for x in myresult:
        a.append(x)
    con.commit()
    con.close()
    if len(a) == 0:
        return {'error':404}
    else:
        return {'id':a[0][0],'username':a[0][1],'phone':a[0][2]}

def id_s(id):
    con = sqlite3.connect('data.db')
    mycursor = con.cursor()
    myresult = mycursor.execute("SELECT * from users WHERE id ='{}' LIMIT 1".format(id))  
    a = []
    for x in myresult:
        a.append(x)
    con.commit()
    con.close()
    if len(a) == 0:
        return {'error':404}
    else:
        return {'id':a[0][0],'username':a[0][1],'phone':a[0][2]}

@app.route('/',methods=['GET'])
def index():
    id = request.args.get('id')
    username = request.args.get('username')
    if request.method == 'GET':
        if id:
            return db.id_s(id)
        elif username:
            return db.username_s(username)
        return {'error':'Query is not correct'}

if __name__ == '__main__':
    app.run(port=80)
