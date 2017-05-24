import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.tododb


@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    redis.incr('hits')
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description'],
	'redis_count': redis.get('hits')
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    db.tododb.delete_many({})
    return redirect(url_for('todo'))

@app.route('/redis_remove', methods=['GET', 'POST'])
def redis_remove():
    redis.set('hits', 0)
    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
