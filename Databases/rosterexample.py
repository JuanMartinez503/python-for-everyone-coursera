import sqlite3
import json
connection = sqlite3.connect('rosterdb.sqlite')


cursor = connection.cursor()
cursor.executescript('''
                     DROP TABLE IF EXISTS User;
                     DROP TABLE IF EXISTS Member;
                     DROP TABLE IF EXISTS Course;
                     CREATE TABLE User (
                         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                         name TEXT UNIQUE
                     );
                     CREATE TABLE Course (
                         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                         title TEXT UNIQUE
                     );
                     CREATE TABLE Member (
                         user_id INTEGER,
                         course_id INTEGER,
                         role INTEGER,
                         PRIMARY KEY (user_id, course_id)
                     );''')
