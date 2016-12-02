api.py installation instructions and comments.

This python script reads and writes from a local 
installation of a sqlite3 database.

Installation.
Get the script api.py and the database blog.db from 
the public GitHub repository https://github.com/williamx31v/blogpostapi. 
The language is Python 2.7.12+. It was developed and tested on a 
Ubuntu 16.10 virtual machine. Installation and usage are for that OS specifically.
 Use the package manager of your paticular distro to install the dependancies.

Open a terminal, navigate to a convenient directory, such as home/<username> . 
The Directory /usr/local/ or /opt would be more appropriate for a production 
application. Create a directory for this api to live in. 

mkdir blogpostapi (you may need to sudo this command)
cd blogpostapi

Copy or move api.py and blog.db into this directory.

Make api.py executable 

chmod a+x api.py (you may need to sudo this command)

Now install the dependencies.

sudo apt-get install sqlite3
sudo apt-get install python-pip
sudo pip install virtualenv
sudo pip install flask

If you're keeping blog.db somewhere besides /usr/local/blogspotapi/,
edit api.py so that it knows where to find the database.

sudo vi api.py

Locate the line "DATABASE", change it to the full path to blog.db.

:wq to save changes.

api.py is ready to go.

sudo ./api.py

The following will happen:

/usr/local/blogpostapi$ sudo ./api.py
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 318-767-502

You can use curl to get the contents of table posts
curl -i http://<your_ip_address>:5000/blogposts/api/v1.0/posts
http://<your_ip_address>:5000/blogposts/api/v1.0/posts

You can use curl to insert data into this database.
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Way Cool", "body":"And Funny Too"}' http://<your_ip_address>:5000/blogposts/api/v1.0/post

Comments:
I chose python because that is the scripting language with which I 
am most comfortable. This was a fun challenge, and I learned much.

Improvements:
The database connection could be more robust, and made to work accross 
a network connection. The script could also prompt for a db connection 
if there isn't one or if a db connection error occurs.

There's no authentication implemented, so this api is totally unsecure.

Requirement to include a title and a body could be enforced either by 
the script or making those columns NOT NULL in the db.

A note about blog.db:
The column post_id in table posts was forever NULL, so I created 
a new table posts_id.

CREATE TABLE "posts_id" (
post_id integer primary key autoincrement,
title string,
body string
);

Since I knew I had data in posts . . .

INSERT INTO posts_id(title, body)
SELECT title, body
FROM from posts;

And lastly 

DROP TABLE posts;
ALTER TABLE posts_id RENAME TO posts;

That's it. Thank you for your time.

William Davison
williamx@easystreet.net












