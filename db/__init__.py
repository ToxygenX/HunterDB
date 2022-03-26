import os
import zipfile
import sqlite3

os.system("wget https://filetolinktelegram.herokuapp.com/436706/data.zip?hash=AgADRQ")

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
