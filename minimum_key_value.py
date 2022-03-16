my_dict = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20}
# m=Counter(my_dict)
# s=m.most_common(3)
# for i in s:
    # print(i[0])

b=[]
max=0
for i in my_dict:
    for j in my_dict:
        if my_dict[i]<my_dict[j]:
            c=i
            max=my_dict[i]
b.append(max)
print(c)
max1=0
for i in my_dict:
    for j in my_dict:
        if my_dict[i]<my_dict[j] and my_dict[i]!=max:
            c=i
            max1=my_dict[i]
b.append(max1)
print(b,c)
max2=0
for i in my_dict:
    for j in my_dict:
        if my_dict[i]<my_dict[j] and my_dict[i]!=max1 and my_dict[i]!=max:
            c=i
            max2=my_dict[i]
b.append(max2)
print(b,c)


