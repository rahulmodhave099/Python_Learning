# Generator :
'''
def run():

    yield 10
    yield 20

ret = run()
print(next(ret))
print(next(ret))
'''
def fun():

    print("Start Fun")
    yield 10
    yield 20
    yield 30
    print("End Fun")
    yield
ret = fun()

for i in fun():
    print(i)

print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))

