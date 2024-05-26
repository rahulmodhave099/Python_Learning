# Creating types List
# 1. list literals

batsman = ["Rohit", "Shubhman", "Virat", "Shreyas", "KLRahul"]
print(batsman)
print(type(batsman))

batRun = ["Rohit", 47, "Shubhman", 80, "Virat", 117, 397, 7.9]
print(batRun)
print(type(batRun))

employee = [{10, "Ashish", 1.5}, {11, "Kanha", 1.7}, {12, "Rahul", 2.0}]
print(employee)
print(type(employee))

player = [{18: "Virat"}, {45: "Rohit"}, {77: "Shubman"}]
print(player)
print(type(player))

# 2. list Constructor

list1 = list()
print(list1)                        # Empty List
print(type(list1))

list2 = list([10, 20, 30, 40, 50])
print(list2)
print(type(list2))

list3 = list((10, 20, 30, 40, 50))          # here we can give any object i.e list,tuple,set,dict
                                            # to the list constructor to convert it into list
print(list3)
print(type(list3))

listdata = [10, 20, 30, 40, 50]

list4 = list(listdata)             # here we can give external defined object name of any datatype i.e list,tuple,set,dict
                                   # to the list constructor to convert it into list
print(list4)
print(type(list4))

listdata = [{10: 20}, {30: 40}, {50: 60}]

list4 = list(listdata)             # here we can give external defined object name of any datatype i.e list,tuple,set,dict
                                   # to the list constructor to convert it into list
print(list4)
print(type(list4))

# 3. comprehension

normList = [num for num in range(1,11)]

print(normList)
print(type(normList))

even_List = [num for num in range(1,11) if num % 2 == 0]

print(even_List)
print(type(even_List))

odd_list = [num for num in range(1,11) if num % 2 == 1]

print(odd_list)
print(type(odd_list))

sqr_List = [num*num for num in range(1,11)]

print(sqr_List)
print(type(sqr_List))


