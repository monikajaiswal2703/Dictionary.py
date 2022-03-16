list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
i=0
b=0
a=[]
while i<len(list1):
    c=list1[i],list2[b]
    a.append(c)
    i+=1
    b+=1
print(dict(a))

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# i=0
# b=-1
# a=[]
# while i<len(list1):
#     c=list1[i],list2[b]
#     a.append(c)
#     i+=1
#     b-=1
# print(dict(a))
