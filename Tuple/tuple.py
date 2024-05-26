# tuple

lang = ("cpp","java","python","JS","Dart",(10.5,20,30,40))

print(lang)
print(type(lang))

#lang[3] = "Go"       Gives error TypeError: 'tuple' object does not support item assignment bcoz tuple is immutable

# Methods in tuple
# 1. count 2. index

print(lang.count("java"))

print(lang.index("JS"))

