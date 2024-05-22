'''
age = int(input("Enter your age : "))

if(age > 18):
    print("Eligible")

print("Out of if ")

# pass statement

if(age > 18):
    pass
print("eligible")

NOTE : 1) Syntax Error : If we miss to write ':' after if() then it gives syntax error.
 NOTE : 1) Indentation Error : If we miss to give space '   ' for new line after if(), 
        then it will not considered as if body and then it gives indentation error

x = int(input("Enter value of x : "))
if(x):
    print("true")


print("Out of if ")

# IF-ELSE

if(x > 20):
    print("x is greator than 20")
else:
    print("x is less than 20")

# Indentation error

if(x > 20):
    print("x is greator than 20")
else:
                    print("x is less than 20")
    print("In else block")

IndentationError: unindent does not match any outer indentation level


if(x > 20):
    print("x is greator than 20")
else:
                    print("x is less than 20")
                    print("In else block")


# Can we use {} in python ?
#Ans : We cannot use {} to define any function or inbuilt class ,
#      but we can use it inside the block of any function or inbuilt class.

if(x > 20) {                          It gives error:  if(x > 20) {
    print("x is greator than 20")                                   ^
                                        SyntaxError: invalid syntax
} else{
    print("x is less than 20")
    print("In else block")
}


if(x > 20):
    print("x is greator than 20")
else:
        print("x is less than 20")
        {
            print("In else block")
        }

y = int(input("Enter the value of y : "))

if(y%2 == 0):
    print("%d is a Even Number " %y)

else:
    print("%d is a Odd number" %y)

'''

# ================= If - else : Assignment 2 ======================================================================
'''
1. WAP to check numbers are divisible by 4 and 5
Print those numbers
Input1: num1 =20
Output:
20 is divisible by 4 and 5
Input1: num1 =15
Output:
15 is not divisible by 4 and 5


num = int(input("Enter a number : "))

if(num%4 == 0 and num%5 == 0):
    print("%d is divisible by 4 and 5"%num)
else:
    print("%d is not divisible by 4 and 5"%num)
'''

'''
2. WAP to determine whether entered angles define a right-angled triangle.
Take three values of angle from the user.
Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
Output:
It is not a right-angle triangle
Input1: angel1 = 90
Input2: angle2 = 60
Input3: angle3 = 30
Output:
It is a right-angle triangle


x,y,z = map(int,input("Enter three angles separated by space : ").split())

if(x+y+z == 180 and ((x == 90 and y != 90 and z != 90) or (x != 90 and y == 90 and z != 90) or (x != 90 and y != 90 and z == 90))):
    print("It is a right-angle triangle")
else:
    print("It is not a right-angle triangle")
'''

'''
3. Take two numbers from users and print the sum of those numbers
Input1: num1 = 10
Input2: num2 = 20
Output: 30 is Eve
n
Input1: num1 = 10
Input2: num2 = 15
Output: No Output


num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if((num1+num2) % 2 == 0):
    print("{} is Even".format(num1+num2))
'''

'''
4. Take a number from the user and check whether it is present in the list. If
it's in the list, print "Available."
List1 = [10, 20, 30, 40, 50]
#input: num = 10
#Output: available
#input num = 15
#Output:No Output

List1 = [10, 20, 30, 40, 50]

num = int(input("Enter Number : "))
if(num in List1):
    print("available")
'''

'''
5. Print the "Core2web" string a number of times entered by the user if the
number is even.
#Input: num = 2
#Output: Core2web
Core2web
#Input: num = 5
#Output: No Output

num = int(input("Enter Number : "))

if(num % 2 == 0):
    for i in range(num):
        print("Core2Web")
'''

'''
6. Write a program that checks if a given number is odd using the "if"
#Input num = 13
#Output: Odd
#Input: num = 12
#Output: No Output

num = int(input("Enter Number : "))
if(num % 2 != 0):
    print("Odd")
'''

'''
7. Take two numbers from the user, check if both are odd and then print the
sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

if(num1%2 != 0 or num2%2 != 0):
    print(num1+num2)
'''

'''
8.Take single character from user check if the ascii value of character is
Even the print character.
#Input char1 = ‘B’
#Output: B
#Input char1 = ‘C’
#Output: No Output

x = input("Enter Single Character : ")

if(len(x) == 1 and ord(x)%2 == 0):
    print(x)
'''

'''
9. Take Two character from user check if the ascii value both of character are
odd then print the sum of ascii values of character
#Input: char1 = ‘A’
char2 = ‘C’
#Output: 132
#Input: char1 = ‘a’
char2 = ‘b’
#Output:No Output

ch1 = input("Enter 1st Character : ")
ch2 = input("Enter 2nd Character : ")

if(len(ch1) == 1 and len(ch2) == 1):
    if(ord(ch1)%2 != 0 and ord(ch2)%2 != 0):
        print(ord(ch1)+ord(ch2))
'''

'''
10. Take the number from user and modulus with 8 if the reminder of the
number is 3 then print reminder.
#Input num = 27
#Output: 3
#Input: num = 10
#Output: No Output
'''

num = int(input("Enter Number : "))

if(num % 8 == 3):
    print(num%8)

