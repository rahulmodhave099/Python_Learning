# To know continue statement more let see one code with pass statement

for i in range(1,11):
    if(i%5 == 0):
        pass
    else:
        print(i)
    print("Hello")

# here in above code pass skips only if else condition but it runs the remaining body of for loop

# But when we use continue statement it will skip all the remaining body content
# and return to for loop for next condition let see below

for i in range(1,11):
    if(i%5 == 0):
        continue
    else:
        print(i)
    print("Hello")

# Thus continue statement skips the all remaining body part and return to main loop
# where as pass statement passes only comparitive condition and continues remaining body part/code

