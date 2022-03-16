# list = ["M", "I", "S", "S", "I", "S", "S", "I", "P", "P", "I",]
# i=0
# d=[]
# while i<len(list):
#     j=0
#     n=[]
#     count=0
#     while j<len(list):
#         if list[i] in list:
#             if list[i]==list[j]:
#                 count+=1
#         j+=1
#     n.append(list[i])
#     n.append(count)
#     if n not in d:
#         d.append(n)
#     i+=1
# print(dict(d))

a="MISSISSIPPI"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)



