
# assert statement is used to handle wrong values and it gives error Assertion Error which we can type

name = input("Enter Your Name : ")
age = int(input("Enter Your age : "))

assert age > 0,".... age negative nastaaa"
if(age > 18):
    print(name,"eligible for voting")
else:
    print(name,"not eligible for voting")