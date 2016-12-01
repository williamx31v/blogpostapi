#!/usr/bin/python

#define modules for import
import sqlite3
import json
from flask import Flask
from flask import jsonify
from flask import request

#define app
app = Flask(__name__)

DATABASE='/home/william/blogpostapi/blog.db'


def insert_blogpost(blogpost):
	con=sqlite3.connect(DATABASE)
	c=con.cursor()
	c.execute("INSERT INTO posts (title,body) VALUES (?,?)")
	con.commit()
	con.close

@app.route('/blogposts/api/v1.0/posts', methods=['GET','POST'])
def result():
	if request.method == 'POST':
		blogpost == request.form['blogpost']
		insert_blogpost(blogpost)
		return "OK"
	else:
		con=sqlite3.connect(DATABASE)
		c=con.cursor()
		c.execute("SELECT * from posts")
		json_get=json.dumps(c.fetchall())
		con.close
		return jsonify({'posts':json_get})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)	

#get all records from table posts
#@app.route('/blogposts/api/v1.0/posts', methods=['GET'])
#def get_posts():
#	if request.method == 'GET':	
#		conn = sqlite3.connect("/home/william/blogpostapi/blog.db")
#		c = conn.cursor()
#		c.execute("SELECT * from posts")
#		json_get=json.dumps(c.fetchall())
#		conn.close
#		return jsonify({'posts':json_get})
#if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0',port=5000)

#post into table posts
#@app.route('/blogposts/api/v1.0/posts/post', methods=['POST'])
#def posts_post():
#	if not request.json or not 'title' or not 'body' in request.json:
#       		abort(400)
#	conn = sqlite3.connect("/home/william/blogpostapi/blog.db")
#	json_post = request.json()
#	c = conn.cursor()
#	c.execute("INSERT into posts (title, body) VALUES (?,?)")
#	conn.close
#	return jsonify({'posts':json_post}), 201
#if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0',port=5000)
