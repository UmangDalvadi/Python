# mutable=can change
# immutable=can nnnnooootttttt change

tp=(1,)#tuple can not change ,immutable
print(tp)

name=["umang","vikash","keval","dhruv"]
print(name)
print(name[::2])

number=[56,45,25,3,20,78]

number.sort()
print(number)

number.reverse()
print(number)

print(number[::3])

number.append(99)
print(number)

print(max(number))

number.insert(2,15) # (index,number)
print(number)

number.remove(15)
print(number)

number.pop() # last element remove
print(number)

number[1]=4444 # will add in index 1
print(number)