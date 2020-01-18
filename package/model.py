#Tushar Borole
#Python 2.7

import sqlite3
import json
with open('config.json') as data_file:
    config = json.load(data_file)

conn=sqlite3.connect(config['database'], check_same_thread=False)
conn.execute('pragma foreign_keys=ON')



def dict_factory(cursor, row):
    """This is an function use to fonmat the json when retirve from the  myswl database"""
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn.row_factory = dict_factory

conn.execute('''CREATE TABLE if not exists patient
(pat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_eye TEXT,
pat_den TEXT,
pat_skin TEXT,
pat_ortho TEXT,
pat_gyn TEXT,
pat_ent TEXT,
pat_first_name TEXT NOT NULL,
pat_last_name TEXT NOT NULL,
pat_city TEXT NOT NULL,
pat_age TEXT NOT NULL,
pat_gender TEXT NOT NULL,
pat_occupation TEXT NOT NULL,
pat_gp TEXT NOT NULL,
pat_date DATE DEFAULT (datetime('now','localtime')),
pat_market TEXT NOT NULL);''')

conn.execute('''CREATE TABLE if not exists doctor
(doc_id INTEGER PRIMARY KEY AUTOINCREMENT,
doc_first_name TEXT NOT NULL,
doc_no INTEGER NOT NULL,
doc_date DATE DEFAULT (datetime('now','localtime')));''')

conn.execute('''CREATE TABLE if not exists appointment
(app_id INTEGER PRIMARY KEY AUTOINCREMENT,
pat_id INTEGER NOT NULL,
doc_id INTEGER NOT NULL,
FOREIGN KEY(pat_id) REFERENCES patient(pat_id),
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id));''')