from heapq import nlargest


test_dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
n=int(input("entder the number"))
r=nlargest(n,test_dic,key=test_dic.get)
print(r)

"without user find min key list"
dictt = {'V': [10, 12],'VI': [10],'VII': [10, 20, 30, 40],'VIII': [20],
'IX': [10,30,50,70],'X': [80]}
m=1
d=[]
for i ,j in dictt.items():
    if len(j)==m:
        d.append(i)
print(d)
