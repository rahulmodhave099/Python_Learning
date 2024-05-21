#Unary operator

x = 10
y = 20

print(+x)           #10
print(-x)           #-10

ans = ++x
#ans2 = x++

print(ans)          # ignores ++ operator which is present before operant
#print(ans2)        # gives error ++ operator which is present after operant

ans3 = x++y

print(ans3)


