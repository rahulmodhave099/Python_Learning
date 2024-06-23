'''
print("Start Code")

empid = 10
name = "Kanha"

try:
    ans = empid + name

except:
    print("Exception handled")

print("End code")


print("Start code")
try:
    num1 = int(input("Enter value for num1 : "))
    num2 = int(input("Enter value for num2 : "))

except ValueError as err:
    print("Exception Handled")

try :
    print(num1 + num2)
except NameError as err:
    print("Exception Handled")

print("End code")


list1 = [10,"kanha",20,"Rahul",30]

try:
    print(list1[int(input("Value for index : "))])
    print(list1[int(input("Value for index : "))])

    add = list1[0] + list1[2]

except (ValueError,IndexError,TypeError) as err:
    print(err)
else:
    print(add)

print("End code")

'''

def voting(name,age):

    if age<18:
        raise ValueError("Not Eligible for voting")
    else:
        print("Thanks for voting")

print("Start Code")

name = input("Enter your name : ")

try:
    age = int(input("Enter your age : "))

except ValueError:
    print("Proper integer value de ")

try:
    voting(name,age)

except ValueError as err:
    print(err)

print("End Code")
