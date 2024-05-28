# Dictionary

# Creating types of dict
# 1. literals

player = {45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul"}

print(player)
print(type(player))

# 2. constructor

team = dict({45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul"})

print(team)
print(type(team))


myinfo = {"name": "Shashi",3 : ["Biencaps", "Core2Web","Incubator"]}
print(myinfo)

# Nested Dict

players = {45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul","next_to_bat": {96:"Shreyas",63:"SKY",8:"Jaddu"}}

print(players)

print(players[18])
print(players["next_to_bat"][63])
#print(players[33])             KeyError: 33 , as 33 key is not present

players[100] = "Bumrah"

print(players)

players["next_to_bat"][8] = "Jadeja"            #Here value of key 8 : "Jaddu" gets replaced with "Jadeja"

print(players)




