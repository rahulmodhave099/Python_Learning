'''
i = 1

while(i < 5):
    print(i)
    i += 1


x = int(input("Enter End point : "))
i = 1

while(i < x+1):
    if(i%5 == 0):
        print(i)
    i += 1
'''
y = int(input("Enter Starting Point : "))

while(y > 0):
    print(y)
    y -= 1
'''
y = int(input("Enter Starting Point : "))

for i in range(y,0,-1):
    print(i)
'''
# Q. We Want the o/p from 10 to 6 Without changing the While condition
x = 10

while(x > 0):
    if(x >= 6):
        print(x)
    x -= 1

# ========== Another Method ====================
x = 10

while(x > 0):
    print(x)
    x -= 1
    if(x == 5):
        x = 0

# ========= Another Method ==================

# Break Statement

x = 10
while(x > 0):
    print(x)
    x -= 1
    if(x == 5):
        break;