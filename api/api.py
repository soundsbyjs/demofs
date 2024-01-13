#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify

# from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# connect to mariadb
import mariadb
import sys

# Connect to MariaDB Platform
# change this to read password from a file or something more secure
try:
    conn = mariadb.connect(
        user="juno",
        password="1359",
        host="localhost",
        port=3306,
        database="video_games"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# Get Cursor
cur = conn.cursor()

cur.execute("SELECT * from game",)

# Print Result-set
for (game) in cur:
    print(game)


# now, the api
app = Flask(__name__)
@app.route('/')
def index():
    # turn this into the thing we need
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()

