#!/usr/bin/python

#define modules for import
import sqlite3
import json
from flask import Flask
from flask import jsonify
from flask import request

#create connecton
conn = sqlite3.connect("/home/william/blogpostapi/blog.db")
c = conn.cursor()

#get all data from table posts
c.execute("SELECT * from posts")

json_get=json.dumps(c.fetchall())


#define app
app = Flask(__name__)

#get all records from table posts
@app.route('/blogposts/api/v1.0/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts':json_get})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)






