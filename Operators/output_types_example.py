# type 1
x = 10
y = 20

print(x)
print()
print(y)

raw = 'this\t\n and that'

# this\t\n and that
print(raw)
raw2 = r'this\t\n and that'

# this\t\n and that
print(raw2)

# type 2   print(string)

print('Core2Web')
print("Core2Web")
print('''Core2Web''')
print("""Core2Web""")

print('Core2Web' + ' Incubator')
print('Core2Web' , ' Incubator')

print(3 * 'Biencqps')

# type 3    print(argument list)

x = 10
y = 20

print(x,y)
#sep
print(x,y, sep=":")
print(x,y, sep=",")
print(x,y, sep="=======")

# end  IMP

print(x)
print(y)

print(x,end=" ")  #using "end" we can print next o/p on same line
print(y)

# type 4    print(formatted output)  like printing line in C programming

x = 10
y = 20.5

# method 1

print("Value of x = %i" % x)
print("Value of x = %d" % x)
print("Value of y = %f" % y)

print("Value of x = %d" , x)
print("Value of y = %f" , y)

# method 2

print("Value of x = {} and Value of y = {}".format(x,y))


