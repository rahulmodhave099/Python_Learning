
def factorial(x):
    ans = 1
    for i in range(1,x+1):
        ans = ans * i
    return ans

x = int(input("Enter value for x : "))

ans = factorial(x)

print(ans)

# ** IMP ** Returning Multiple values in Function
def fun(x,y,z):
    return x+10,y+10,z+10

x = int(input("Enter value for x : "))          #10
y = int(input("Enter value for y : "))          #20
z = int(input("Enter value for z : "))          #30


a,b,c = fun(x,y,z)
print(a)                    #20
print(b)                    #30
print(c)                    #40

retval = fun(x,y,z)

print(type(retval))         #<class 'tuple'>

print(retval)               #(10,20,30)

for i in retval:            #10
    print(i)                #20
                            #30