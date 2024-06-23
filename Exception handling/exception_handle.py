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
'''


