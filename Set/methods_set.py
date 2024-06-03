# Methods of Set

setData = {1,2,3,4}
print(setData)

# 1. add

setData.add(5)
print(setData)

# 2. copy

setData2 = setData.copy()
print(setData2)

# 3. difference

setData2 = {4,5,7,8,9}

setData3 = setData.difference(setData2)

print(setData3)

# 4. difference_update
print(setData)
setData.difference_update(setData3)

print(setData)

# 5. discard

setData = {1,2,3,4,5}
print(setData)

setData.discard(3)

print(setData)
# 6. intersection
setData = {1,2,3,4,5}
print(setData)
print(setData2)

setData3 = setData.intersection(setData2)

print(setData)
print(setData2)
print(setData3)
# 7. intersection_update

setData.intersection_update(setData3)
print(setData)

# 8. isdisjoint
setData = {1,2,3,4}
setData2 = {5,6,7,8}

print(setData.isdisjoint(setData2))

setData = {1,2,3,4,5}
setData2 = {4,5,6,7,8}

print(setData.isdisjoint(setData2))

# 9. issubset
setData = {1,2,3,4}
setData2 = {3,4,5,6,1,2}

print(setData.issubset(setData2))

# 10. issuperset
setData = {1,2,3,4}
setData2 = {3,4,5,6,1,2}
print(setData.issuperset(setData2))

setData = {1,2,3,4}
setData2 = {3,4,1,2}
print(setData.issuperset(setData2))

# 11. symmetric_difference
setData = {1,2,3,4,5}
setData2 = {4,5,6,7,8}

setData3 = setData.symmetric_difference(setData2)

print(setData3)
# 12. symmetric_diffference_update
setData.symmetric_difference_update(setData2)
print(setData)

# 13. union
setData = {1,2,3,4,5}
setData2 = {4,5,6,7,8}

setData3 = setData.union(setData2)

print(setData3)

# 14. update

print(setData)
print(setData2)

setData.update(setData2)

print(setData)
print(setData2)

# 15. pop
setData1 = {1,2,3,4,5,6}
setData1.pop()
print(setData1)

setData1 = {10,20,30,40}
setData1.pop()
print(setData1)

# 16. remove
setData1 = {10,20,30,40}
setData1.remove(20)
print(setData1)

# 17. clear

setData1.clear()
print(setData1)                             #set()