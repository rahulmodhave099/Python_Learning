# Bytes Data Type

listData = [10,20,30,40,50]

byteData = bytes(listData)

print(listData)
print(byteData)

for i in byteData:
    print(i)

# Trying to modify the value of byteData

'''byteData[2] = 200
for i in byteData:
    print(i)                # Gives error bcoz bytes are immutable thus e need to use bytearray'''

byteData1 = bytearray(listData)
byteData1[2] = 200

for i in byteData1:
    print(i)

