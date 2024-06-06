# String Methods

# 1. capitalize : Return string by changing first letter into capital.
'''
str1 = "Core2web Incubator"
print(str1)

print(str1.capitalize())

# 2. casefold : It converts all letters into small letters.
str1 = "Core2web Incubator"
str2 = "core2web Incubator"

print(str1.casefold())                  #core2web incubator

print(str1 == str2)                     #False becoz str2 have small 'c' as str1 have capital 'C'

print(str1.casefold() == str2.casefold())     #True bcoz casefold() converts all letters into small letters

# 3. center(width,fillchar =" ") : Put string in center by giving  width and fillchar.

str1 = "core2web"

print(str1.center(12))                      # it uses space if fillchar is not given.

print(str1.center(12,"*"))

# 4. count(x,start,end) :

str1 = "Core2web Incubator"

print(str1.count("b"))

print(str1.count("b",0,8))

# 5. endswith(suffix,start,end) ::

print(str1.endswith("eb"))
print(str1.endswith("eb",2,8))

# 6. expandtabs(tabsize) :

str1 = "Core2web\tIncubator"

print(str1)

print(str1.expandtabs(8))

# 7. find(sub,start,end) :

# 8. format(args) :

str1 = input("Enter main string : ")
sub = input("Enter sub string : ")
c = 0

if sub in str1:
    print(sub + " Found at index {} ".format(str1.index(sub)))
else:
    print(sub + " Not found ")


# using find() method

n = str1.find(sub)
if(n == -1):
    print(sub + " Not Found")
else:
    print(sub + " Found at index {} ".format(n))

m = str1.rfind(sub)             # rfinds() used to check the substring found from right side
if(n == -1):
    print(sub + " Not Found")
else:
    print(sub + " Found at index {} ".format(m))

# Write python code to find out index of second occurance of substring "Geeks" from a string "Geeks for Geeks Geeks"

str1 = "Geeks for Geeks Geeks"
sub = "Geeks"

first_occ = str1.find(sub)
sec_occ = str1.find(sub,first_occ+1)

print(sub + " Second Occurance Found at index {} ".format(sec_occ))


# Write python code to find out index of third occurance of substring "Geeks" from a string "Geeks for Geeks Geeks"

str1 = "Geeks for Geeks Geeks"
sub = "Geeks"

c = 0
index = -1

for x in range(len(str1)):
    index = str1.find(sub,index+1)
    if(index != -1):
        c+=1
        if(c == 3):
            print(sub + " Third Occurance Found at index {} ".format(index))
            break
    else:
        print(sub + " Not Found")

# Write a python code to find out the index of third occurance of substring "Geeks"
# from the string "Geeks for Geeks Geeks" without using find() inbuilt method

str1 = "Geeks for Geeks Geeks"
sub = "Geeks"

c = 0

for i in range(len(str1)):
    if(str1[i:i+len(sub)] == sub):
        c += 1
        if(c == 3):
            print(sub + " Third Occurance Found at index {} ".format(i))
        else:
            print(sub + " found only {} times ".format(c))
    else:
        print(sub + " Not Found ")
'''

# 9. index() : It returns the index value where substring is found.

# 10. isalnum : Returns True if string contains characters or numbers , False otherwise.

# 11. isalpha : Return True if string contains only alphabets , otherwise False.

# 12. isascii :  Returns True if all characters in the string are ASCII , else it returns false.
#                ASCII characters have code points in the range U+0000 - U007F.

# 13. isdecimal : Returns True if all characters in the string are decimal , else returns false.

# 14. isdigit : Returns True if all characters in the string are digits , else returns false.

# 15. islower : Returns True if all characters in the string are lowercase, else false.

# 16. isnumeric : Returns True if all characters in the string are number , else false.

# 17. isprintable : Returns True if string is printable , else false.

# 18. isspace : Returns True if string includes space , else false.

# 19. istitle : Returns true if First character of string is capital , else false.

# 20. isupper : Return True if all characters of string is uppercase (Capital) , else false.

# 21. join(iterable,/) :

str1 = "core2web"

print("-".join(str1))

list1 = ["core2web","incubator","biencaps"]

print("-".join(list1))

# 22. ljust(width,fillchar='') : Left side padding is done using specified fill character.(Default fillchar is a space.)

# 23. rjust(width,fillchar='') : Right side padding is done using specified fill character.(Default fillchar is a space.)

print(str1.ljust(12,"$"))

print(str1.rjust(12,"$"))

# 24. lower : It returns copy of a string converted into lowercase.

# 25. strip : Remove the white spaces from the string.

# 26. lstrip : Remove the white spaces from the left side of the string.

# 27. rstrip : Remove the white spaces from the right side of the string.

str1 = "    core2web    "

print(str1)
print(str1.strip())

print(str1.lstrip())

print(str1.rstrip())

# 28. partition(sep) : It divides the string into  parts using the given separator (substring).
# It search for given separator in the string and if it found it separates before separator , given separator
# and after separator into 3 string and return it into tuple.
# If the separator not found then, it returns a tuple with one given string and remaining 2 empty strings.

str1 = "core2webincubator"

print(str1.partition("web"))
print(str1.partition("hash"))
print(str1.rpartition("hash"))

# 29. replace(old,new,count=-1): It returns copy of string where all occurance of old substring is replaced with new.
#                                Count -1 is default where all occurances gets replace.
#                                If the optional cont is given , then the first occurances till count gets replace.

str1 = "Geeks for Geeks Geeks"

print(str1)
print(str1.replace("eek","oat"))
print(str1.replace("eek","oat",1))
print(str1.replace("eek","oat",2))

# 30. split :

str1 = "core2web incubator biencaps"
str2 = "core2web,incubator,biencaps"

print(str1.split())
print(str1.split(","))
print(str2.split())
print(str2.split(","))

# IMP

x = int(input("Enter 1st value : "))
y = int(input("Enter 2nd value : "))
z = int(input("Enter 3rd value : "))

print(x+y+z)

x,y,z = [int(val) for val in input("Enter three int values : ").split(" ")]

print(x+y+z)


