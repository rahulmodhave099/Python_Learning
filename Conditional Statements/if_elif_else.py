'''
num = int(input("Enter Number : "))

if (num > 0):
    print("{} is Positive number ".format(num))

elif (num < 0) :
    print(" %d is Negative Number" %num)

else:
    print("Number %d is Zero"%num)


no = int(input("Enter Number : "))

print("Square of {} is : {} ".format(no,no**2))

if(no**2 % 2 == 0):
    print("Square of {} is {} which is a Even Number ".format(no,no**2))

else:
    print("Square of {} is {} which is a Odd Number ".format(no,no**2))
'''

# ================= If - else : Assignment 1 ======================================================================

'''
1. Program 1: Write a Program to Find a Maximum between two numbers
Input: 1 2
Output: 2 is Max number between 1 & 2


x = int(input("Enter first number : "))
y = int(input("Enter second number : "))

if(x > y):
    print("{} is Max number between {} & {}".format(x,x,y))
elif(y > x):
    print("{} is Max number between {} & {}".format(y,x,y))
else:
    print("Both numbers {} & {} are equal".format(x,y))
'''

'''
2. Program 2: Write a Program to check whether the number is Negative,
Positive or equal to Zero.
Input: -2
Output: -2 is the negative number

x = int(input("Enter number : "))

if(x > 0):
    print("%d is the positive number"%x)
elif(x < 0):
    print("%d is the negative number"%x)
else:
    print("%d is equal to Zero"%x)
'''
'''
3. Program 3: Write a Program to Find whether the number Is Even or Odd
Input: 4
Output: 4 is an Even Number!

x = int(input("Enter number : "))

if(x%2 == 0):
    print("%d is an even number"%x)
else:
    print("%d is an odd number"%x)
'''
'''
4. Program 4: Write a Program to check whether the number is divisible by 5
or not.
Input: 55
Output: 55 is divisible by 5

x = int(input("Enter number : "))

if(x%5 == 0):
    print("%d is divisible by 5"%x)
else:
    print("%d is not divisible by 5"%x)
'''

'''
5. Program 5: Write a Program to take an integer ranging from 0 to 6 and print
corresponding weekday (week starting from Monday)
Input: 2
Output: Wednesday.

week = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}

x = int(input("Enter the number ranging from 0 to 6 : "))

assert (x >= 0 and x<=6),".... Value Should between 0 to 6"

print(week[x])
'''


'''
6. Program 6: Write a Program to check whether the Character is Alphabet or
not.
Input: v
Output: v is an alphabet.

x = input("Enter Single Value : ")


if(ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x)<= 122):
    print("%s is an alphabet"%x)

else:
    print("%s is not an alphabet"%x)
    
# OR

if ((len(x) == 1) and ('a' <= x <= 'z' or 'A' <= x <= 'Z')):
    print("%s is an alphabet"%x)
    
else:
    print("%s is not an alphabet"%x)
    
'''
'''
7. Program 7: Write a Program to take a number of months and print the number of
days in that month.
Input: 4
Output: April is a 30-day month.
'''

x = int(input("Enter a number between 1 to 12 : "))
mon = [{"month":"January","days":31},{"month":"February","days":28},{"month":"March","days":31},
         {"month":"April","days":30},{"month":"May","days":31},{"month":"June","days":30},
         {"month":"July","days":31},{"month":"August","days":31},{"month":"September","days":30},
         {"month":"October","days":31},{"month":"November","days":30},{"month":"December","days":31}]

if(x >= 1 and x <= 12):
    print("{} is a {}-day month.".format(mon[x-1]['month'],mon[x-1]['days']))

else:
    print("Selected wrong Number.....")


'''
8. Program 8: Write a program to check whether the number is greater than 10 or
not
Input: 12
Output: yes 12 is greater than 10
Input: 2
Output: no 2 is less than 10

x = int(input("Enter Number : "))

if(x > 10):
    print("Yes %d is greater than 10"%x)
elif(x < 10):
    print("No %d is smaller than 10"%x)
else:
    print("%d is equal to number 10"%x)
'''
'''
9. Program 9: Write a program to check whether the input character is a vowel or
consonant
Input: ‘a’
Output: vowel
Input: ‘b’
Output: consonant

x = input("Enter a Single character : ")

assert ((ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x) <= 122)),"......Enter Single Character Onlyyyyy"

vowels = ['a','e','i','o','u','A','E','I','O','U']

if(x in vowels):
    print("Vowel")
else:
    print("Consonant")

'''
'''
10. Program 10: WAP that determines whether a given input year is a leap year or no



year = int(input("Enter Year : "))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
if(year%4 == 0 and year%100 != 0):
    print("%d is Leap Year"%year)
    
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
elif(year%400 == 0):
    print("%d is Leap Year"%year)

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("%d is not a Leap Year"%year)
'''