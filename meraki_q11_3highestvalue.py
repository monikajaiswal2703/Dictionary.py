my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
m=0
for i in my_dict:
    if my_dict[i]>m:
        c=i
        m=my_dict[i]
print(m,c)
# m1=0
# for i in my_dict:
#     if my_dict[i]>m1:
#         if my_dict[i]<m:
#             m1=my_dict[i]
# print(m1)
# m2=0
# for i in my_dict:
#     if my_dict[i]>m2:
#         if my_dict[i]<m1:
#             if my_dict[i]<m:
#                 m2=my_dict[i]
# print(m2)
# d=[m1,m2,m]
# print(d)

