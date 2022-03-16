dictt = {'V': 10,'VI': 10,'VII': 40,'VIII': 20,'IX': 70,'X': 80,'XI': 40,'XII': 20, }
d={}
for i,j in dictt.items():
    if j in d:
        d[j]+=1
    else:
        d[j]=1
print(d)