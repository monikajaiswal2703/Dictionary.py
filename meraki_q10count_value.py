dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# a=dict1.values()
# print((a))
c=0
for i in dict1:
    for j in range(len(dict1[i])):
        c+=1
print(c)