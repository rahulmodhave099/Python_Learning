# Methods in dictionary

players = {45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul",96:"Shreyas",63:"SKY",8:"Jaddu"}
print(players)


# Access methods
# 1. get 2. items 3. keys 4. values

print(players.get(18))

print(players.items())

for key,value in players.items():
    print(key,"#",value,end="  ;  ")

print()
print(players.keys())
print(players.values())

# Delete methods
# 1. pop 2. popitem 3. clear

print(players)

players.popitem()

print(players)

players.pop(77)

print(players)

players.clear()

print(players)


# operation methods
# 1. copy 2. update 3. setdefault 4. fromkeys

players = {45:"Rohit",77:"Shubman",18:"Virat",1:"KLRahul",96:"Shreyas",63:"SKY",8:"Jaddu"}

newData = players.copy()

print(players)
print(newData)

players[18] = "Kohli"

print(players)
print(newData)

data = {63:"Surya",33:"Hardik"}

players.update(data)

print(players)

val = players.setdefault(18,"Kohli")
print(players)                          # no change
print(val)

val = players.setdefault(19,"Kohli")
print(players)                          # append kohli
print(val)

lang = ["ReactJS","Flutter","Springboot"]

teacher = "Shashi"

print(players.fromkeys(lang,teacher))