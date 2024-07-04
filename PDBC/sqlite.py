# creating table in sqlite

import sqlite3

conn = sqlite3.connect("IPL.db")

cursorObj = conn.cursor()

createTable = '''
    create table Players(
    jerno INTEGER(5) NOT NULL PRIMARY KEY,
    playername VARCHAR2(20),
    teamname VARCHAR2(10),
    gender CHAR(1),
    country VARCHAR2(20));
'''

cursorObj.execute(createTable)

conn.close()