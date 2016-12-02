#!/usr/bin/python

#define modules for import
import sqlite3
import json
from flask import Flask, request, jsonify
#from flask import request

#define app
app = Flask(__name__)

#set the database path
DATABASE='/home/william/blogpostapi/blog.db'

#define the api post endpoint
@app.route('/blogposts/api/v1.0/post', methods=['POST'])
def post():
	if not request.json:
		abort(400)
	new_post = request.json
	columns = ', '.join(new_post.keys())
	vals = '"'+'", "'.join(new_post.values())
	query = 'INSERT INTO posts (%s) VALUES (%s")' % (columns, vals)
	con=sqlite3.connect(DATABASE)
	c=con.cursor()
	c.execute(query)
	con.commit()
	con.close
	return "OK"

#define the get endpoint
@app.route('/blogposts/api/v1.0/posts', methods=['GET'])
def get():
	con=sqlite3.connect(DATABASE)
	c=con.cursor()
	c.execute('SELECT * from posts')
	json_get=json.dumps(c.fetchall())
	con.close
	return jsonify(posts=json_get)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)	


