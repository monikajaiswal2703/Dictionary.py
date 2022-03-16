"assending order"
d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in d:
    for j in d:
        if d[i]<d[j]:
            d[i],d[j]= d[j],d[i]
print(d) 
"deccending order"
# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# for i in d:
#     for j in d:
#         if d[i]>d[j]:
#             d[i],d[j]= d[j],d[i]
# print(d) 

# s=sorted(d.keys())
# print(s)

# n=int(input("enter number"))
# if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0 or n==2 or n==3 or n==5 or n==7:
#     print(n,"is pm ")
# else:
#     print(n,"is no pm ")



