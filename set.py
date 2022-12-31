s=set([1,2,3])
s.add(8)
print(type(s))
print(s)

s=set() #set - ignore same value
s.add(1)
s.add(1)
s.add(2)
print(s)

s1=s.union({4,5})
print(s1)

s2=s.intersection(s,s1)
print(s2)

s1.remove(4)
print(s1)
