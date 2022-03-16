dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic={}
for i in (dic1,dic2,dic3):
    dic.update(i)
for i in dic:
    if i in dic1:
        if i in dic2:
            dic.update({i:dic1[i]+dic2[i]})
print(dic)

# l1=[1,5,10,12,16,20]
# l2=[1,2,10,13,16]
# l1.extend(l2)
# m=[]
# for i in l1:
#     if i not in m:
#         m.append(i)
# print(sorted(m))