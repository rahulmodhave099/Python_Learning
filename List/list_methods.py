
# Accessing elements from list
# 1. index
# 2. slicing

player = ["Rohit","Shubman","Virat","Shreyas","KLRahul"]

print(player[0])            #Rohit
print(player[2])            #Virat
print(player[4])            #KLRahul

print(player[-3])           #Virat
print(player[-2])           #Shreyas
print(player[-4])           #Shubman

print(player[2::])          #["Virat","Shreyas","KLRahul"]
print(player[2:4:2])        #["Virat"]
print(player[:5:3])         #["Rohit","Shreyas"]
print(player[4:2:-1])       #["KLRahul","Shreyas"]

# Methods from list

# Access methods

# 1. append  2. extend 3. insert

player = ["Rohit","Shubman","Virat","Shreyas","KLRahul"]

print(player)

player.append("SKY")

print(player)

player.extend(["Jadeja","Bumrah","Shami"])

print(player)

player.insert(3,"Hardik")

print(player)


# Deletion
# 1. remove 2. pop 3. clear

player.remove("SKY")
print(player)

player.pop()
print(player)

player.pop(4)
print(player)

player.clear()

print(player)

# operation

# 1. count 2. index 3. reverse 4. sort 5. copy

player = ["Rohit","Shubman","Virat","Shreyas","KLRahul","SKY","Jadeja","Bumrah","Shami","Jadeja"]

print(player.count("Jadeja"))
print(player.index("Jadeja"))

player.reverse()

print(player)

player.sort()

print(player)

batsman = player.copy()
print(batsman)

