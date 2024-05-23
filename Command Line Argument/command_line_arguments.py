import sys

print(sys.argv)

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

add = 0

for i in range(1,len(sys.argv)):
    add = add + int(sys.argv[i])

print(add)


add = 0

for i in range(1,len(sys.argv)):
    if(int(sys.argv[i]) % 2 == 0):
        add = add + int(sys.argv[i])

print(add)
