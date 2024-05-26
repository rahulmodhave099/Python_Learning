# Nested List

lang = ["Cpp","Java","Python",["Go","Rust","Dart"]]

print(lang[1])
print(lang[3])
print(lang[3][1])

# Shallow Copy & Deep Copy : Works for only nested list

newList = lang.copy()

print(lang)
print(newList)

lang[3][1] = "JavaScript"

print(lang)
print(newList)

# In Above code we have changed the data from index lang[3][1] from list lang
# and the the data from copied list newList is also get changed automatically same as the orignal list lang.

# Here we have changed the data from lang list but automatically the data from the copied list neList is also changed
# becoz the list has been copied with the help of shallow copy method.

# Shallow Copy : In this type , the nested copied list gets changed automatically as we do changes to orignal nested list.

# Thus we can use deep copy concept as below to overcome on shallow copy.
# Deep copy : In this type , the changes occured on orignal list deos not affect on copied list.

import copy as cp

lang = ["Cpp","Java","Python",["Go","Rust","Dart"]]

newList = cp.deepcopy(lang)

print(lang)
print(newList)

lang[3][1] = "JavaScript"

print(lang)
print(newList)

# As we can see in above example , the copied list newList element "Rust" does not get replace with "JavaScript"   

