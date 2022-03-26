from flask import Flask
from flask import request

from . import db

app = Flask(__name__)

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
