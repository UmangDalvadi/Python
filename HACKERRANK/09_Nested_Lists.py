n=int(input())

res=[]
grade=[]

for i in range (n):
    name=input()
    mark=float(input())
    res.append([name,mark])
    grade.append(mark)
    
grade=sorted(set(grade))

m=grade[1]

name=[]

for i in res:
    if m==i[1]:
        name.append(i[0])
        
name.sort()

for i in name:
    print(i)
        


        
        
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

