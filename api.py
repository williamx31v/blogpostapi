#!/usr/bin/python

#define modules for import
import sqlite3
import json
from flask import Flask
from flask import jsonify
from flask import request

#define app
app = Flask(__name__)

#set the database path
DATABASE='/home/william/blogpostapi/blog.db'


@app.route('/blogposts/api/v1.0/posts', methods=['GET','POST'])
def result():
	if request.method == 'POST':
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

	else:
		con=sqlite3.connect(DATABASE)
		c=con.cursor()
		c.execute("SELECT * from posts")
		json_get=json.dumps(c.fetchall())
		con.close
		return json_get


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)	


