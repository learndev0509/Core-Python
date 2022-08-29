t=(1,2,1.1,True,"tops",[10,20,30],10,"python",1,2)

print(t)
print(t.count(1))
print(t.index(10))
print(t[5])
t[5].append(40)
print(t)

for i in t:
    print(i)
print(10 in t)
