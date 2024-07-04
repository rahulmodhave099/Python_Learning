# creating table in sqlite

import sqlite3

conn = sqlite3.connect("IPL.db")

cursorObj = conn.cursor()

"""
createTable = '''
    create table Players(
    jerno INTEGER(5) NOT NULL PRIMARY KEY,
    playername VARCHAR2(20),
    teamname VARCHAR2(10),
    gender CHAR(1),
    country VARCHAR2(20));
'''

cursorObj.execute(createTable)


# insert into table

player1 = '''insert into Players values(18,"Virat","RCB","M","India")'''
player2 = '''insert into Players values(33,"Warner","DC","M","Australia")'''
player3 = '''insert into Players values(41,"Mandhana","RCB","F","India")'''
player4 = '''insert into Players values(45,"Rohit","MI","M","India")'''
player5 = '''insert into Players values(12,"Perry","MI","F","England")'''
player6 = '''insert into Players values(93,"Bumrah","MI","M","India")'''

cursorObj.execute(player1)
cursorObj.execute(player2)
cursorObj.execute(player3)
cursorObj.execute(player4)
cursorObj.execute(player5)
cursorObj.execute(player6)

conn.commit()
"""

# fetching / reading data from table

reading = '''select * from Players'''

cursorObj.execute(reading)

playerData = cursorObj.fetchall()

print(playerData)

print(type(playerData))

for i in playerData:
    print(i)

conn.close()