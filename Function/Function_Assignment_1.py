'''
1. What is the output of the following function?

def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner()

ans = outer()
print(ans)              # Hello, I'm the inner function!
'''

'''
2. What is the output of the following function? (dry run compulsory)

def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner

retObj = outer()
print(retObj)               # <function outer.<locals>.inner at 0x0000015FD4CE54E0>
retInner = retObj()
print(retInner)             # Hello, I'm the inner function!
'''

'''
3. WAP for function returns the array of factorial of the element
● Pass the array to the function
Input: [1, 2, 3, 4, 5]
Output:[1, 2, 6, 24, 120]

def factorial(list1):
    x = 0
    for i in list1:
        ans = 1
        for j in range(1,i+1):
            ans *= j
        list1[x] = ans
        x += 1
    return list1

list1 = [1,2,3,4,5]
ans = factorial(list1)

print(ans)
'''

'''
4. WAP for a function that returns the count of the search element in the list
Input:
listData = [1, 2, 3, 3, 4, 5, 3]
searchEle = 3
Output: 3 found in list 3 time

def count(listData):
    searchfile = int(input("Enter the Number to be Search : "))
    cnt = 0
    for i in listData:
        if(searchfile == i):
            cnt += 1
    print("{} found in list {} times".format(searchfile,cnt))
listData = [1, 2, 3, 3, 4, 5, 3]

count(listData)
'''

'''
5. Write the parent function that includes the nested functions digitCount,
evenDigitCount, and oddDigitCount. provide a number to th functions Then, call
all functions and ﬁll in the return value in the list.
Input:
Num = 12345
Output: [5, 2, 3]
Solution : 

def count():

    def digitCount(*args):
        cnt = 0
        for i in args:
            cnt += 1
        return cnt

    def evenDigitCount(*args):
        cnt = 0
        for i in args:
            if(i%2 == 0):
                cnt += 1
        return cnt

    def oddDigitCount(*args):
        cnt = 0
        for i in args:
            if(i%2 == 1):
                cnt += 1
        return cnt

    return digitCount,evenDigitCount,oddDigitCount

a,b,c = count()

ans1 = a(1,2,3,4,5)
ans2 = b(1,2,3,4,5)
ans3 = c(1,2,3,4,5)

list1 = [ans1,ans2,ans3]

print(list1)

'''

'''
6. Python program that deﬁnes a parent function with two nested functions
(myIndex and myPalindrome). The program prompts the user to choose between
these two functions and then calls the selected function based on the user's
input.
Input:
Choice = 1
listData = [1, 2, 3, 4, 5, 6]
searchEle = 2
Output: 1
Input:
Choice = 2
Num = 141
Output: True


def outer():

    def myIndex(listData,sElement):
        for i in listData:
            if(sElement == i):
                cnt = listData.index(sElement)
                return cnt
            else:
                cnt = "Element Not Found"
    def mynumPalindrome(num):
        q = num
        rem = 0
        ans = 0
        while(q!=0):
            rem = q % 10
            ans = ans*10 + rem
            q //= 10
        return ans
    def mystrPalindrome(string):
        length = len(string)
        ans = ""
        for i in range(length-1,-1,-1):
            ans = ans + string[i]
        if(string==ans):
            return True
        else:
            return False


    return myIndex,mynumPalindrome,mystrPalindrome

listData = [1,2,3,4,5,6,7,8,9]
a,b,c = outer()
print("1. Find Count of number in List with function myIndex() ")
print("2. Find number is palindrome or not with function mynumPalindrome() ")
print("3. Find String is palindrome or not with function mystrPalindrome() ")
ch =int(input("Enter your choice between 1 , 2 , 3 : "))
if(ch == 1 or ch==2 or ch==3):
    if(ch==1):
        sElement = int(input("Enter Search Element : "))
        ans = a(listData,sElement)
        print(ans)
    elif(ch==2):
        num = int(input("Enter Number Which is greater than 99 only : "))
        if(num>99):
            ans = b(num)
            if (num == ans):
                print("True")
            else:
                print("False")
        else:
            print("Entered number less than 99 plz try again.....")
    else:
        string = input("Enter the String to check palindrome : ")
        ans = c(string)
        print(ans)
else:
    print("Entered Wrong Choice ..... Try Again")
'''


'''
7. WAP defines a class Sum with a mySum method that returns the sum of two numbers.
The program creates two class objects, takes user input to set values for each object,
prints the return sum for both objects, and then determines whether the total sum is even
or odd.
Input:
Object1 input:
Num1 = 3
Num2 = 5
Object input:
Num1= 4
Num2 =5
Output: Sum is Odd 17

class Sum:

    def __init__(self):
        self.add = 0

    def mySum(self,a,b):
        self.add = a + b
        return self.add

sum1 = Sum()
sum2 = Sum()

add1 = sum1.mySum(5,3)
add2 = sum2.mySum(5,4)

add = add1 + add2

if(add % 2 == 0):
    print("Sum is even {} ".format(add))
else:
    print("Sum is odd {} ".format(add))
'''

'''
8. Write a realtime example of oop which contains the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method
'''
class IPL:
    leagueName = "IPL"

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2

    def todayMatch(self):
        print("Today {} Match {} vs {} at 7:30 PM on StartSports1 HD".format(self.leagueName,self.team1,self.team2))

match = IPL("Mumbai_Indians","Chennai_Super_Kings")

match.todayMatch()


'''
9. Write a real-time example of OOP on IPL cricket by the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method

class IPL:
    leagueName = "IPL"

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2

    def todayMatch(self):
        print("Today {} Match {} vs {} at 7:30 PM on StartSports1 HD".format(self.leagueName,self.team1,self.team2))

match = IPL("Mumbai_Indians","Chennai_Super_Kings")

match.todayMatch()

'''

'''
10. Write a program in which you have to write a _new_ user-defined function that
creates a new instance of a class.
'''

class IPL:
    leagueName = "IPL"

    def __new__(cls,team1,team2):
        return super().__new__(cls)

    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2

    def todayMatch(self):
        print("Today {} Match {} vs {} at 7:30 PM on StartSports1 HD".format(self.leagueName,self.team1,self.team2))

match = IPL("Mumbai_Indians","Chennai_Super_Kings")

match.todayMatch()