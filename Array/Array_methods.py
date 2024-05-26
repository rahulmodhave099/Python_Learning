import array as arr
#Methods of Array

# 1. append
data = arr.array('b',[10,20,30,40,50])

print(data)                 #array('b', [10, 20, 30, 40, 50])
data.append(40)             #
print(data)                 #array('b', [10, 20, 30, 40, 50, 60])

# 2. buffer_info() : It gives address and length of array (address , length)

print(data.buffer_info())   #(2701905199856, 5)
#print(id(data))

# NOTE : As we print address by buffer_info() and id() both are different bcoz id gives the address of the array named as data
# where buffer_info() gives the address of 1st element of array

# 3. count() : Gives the element number of count present in array but we have to pass one argument to method count()

print(data.count(40))

# 4. extend() : it adds more than one element at the end of array

data.extend([60,70])
print(data)

# 5. fromlist() : It adds list at the end of the array

listdata = [10,20,30,40]

arrData = arr.array('i',[100,200,300,400])

print(arrData)
arrData.fromlist(listdata)
print(arrData)

# 6. index() : It gives the index(position) of the given element to the method index() from the array

print(arrData.index(300))

# 7. insert() : We can add element in array at any position of array by providing index and element to method insert(index,element)

arrData.insert(4,500)
print(arrData)


# 8. pop() : It removes the last element of the array

arrData.pop()
print(arrData)

# 9. remove() : It removes the given element which occur first in array.

arrData.remove(200)
print(arrData)

# NOTE : If above array has two same elements 200 ,then it will remove the one that first occur and remains the other ones.

# 10. reverse() : reverse the array

arrData.reverse()
print(arrData)

# 11. tolist() : converts array into list

copyList = arrData.tolist()

print(copyList)
print(arrData)


#Attributes of array

# 1. typecode


# 2. itemsize : Gives size of the type of data(typecode)

data = arr.array('b',[10,20,30,40,50])

print(data.itemsize)