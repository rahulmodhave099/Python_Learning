
# range class

for x in range(5):          #Single argument (Stop)
    print(x)

for x in range(1,6):        #Double arguments (Start,Stop)
    print(x)

for x in range(10,5,-1):    #Triple arguments (Start,Stop,Step)
    print(x)

for x in range(1,15,3):
    print(x)


x = int(input("Enter Start Point : "))
y = int(input("Enter End Point : "))

for a in range(x,y+1):
    print(a)

for i in range(10,3,-2):
    print(i)

a = int(input("Enter Start No : "))
b = int(input("Enter Stop No : "))

for i in range(a,b+1):
    if (i%2 == 0):
        print("%d is Even" %i)
    else:
        print("%d is Odd" %i)


m = int(input("Enter starting point : "))
n = int(input("Enter ending point : "))

for i in range(m,n+1):
    if(i%4 == 0 and i%5 ==0):
        print(i)


for i in range(1,5):
    print(i)

print(i)


