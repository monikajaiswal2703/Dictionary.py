# a={"name":"monika","surname":"jaiswal","age":21}
# a.pop('age')
# print(a)

# a={"name":"monika","surname":"jaiswal","age":21}
# a.popitem()
# print(a)

# a={"name":"monika","surname":"jaiswal","age":21}
# del(a["age"])
# print(a)

# a={"name":"monika","surname":"jaiswal","age":21}
# a.clear()
# print(a)


# a={"name":"monika","surname":"jaiswal","age":21}
# a.copy()
# print(a)

# a={"name":"monika","surname":"jaiswal","age":21}
# b=a.keys()
# print(b)

# a={"name":"monika","surname":"jaiswal","age":21}
# b=a.values()
# print(b)

# a={"name":"monika","surname":"jaiswal","age":21}
# a.update({"age":20})
# print(a)

# a={"name":"monika","surname":"jaiswal","age":21}
# print(a.items())

# marks = {'Physics':67, 'Maths':87}
# print(marks.get('Physics'))

# # Using get() results in None
# {print('Salary: ', marks.get('salary'))


# # Using [] results in KeyError
# print(marks['salary'])

# "using fromkeys"
# keys = {'a', 'e', 'i', 'o', 'u' }
# vowels=dict.fromkeys(keys,'monika')
# print(vowels)

# marks={'Physics':67, 'Maths':87,'age':22}
# # age=marks.setdefault("monika",'jaiswal')
# # print(age)
# del marks['Maths']
# print(marks)

# marks.clear()
# print(marks)

# marks.pop('Maths')
# print(marks)

# a={"india":"delhi","UP":"lacknow","US":"america"}
# b={"franc":"pesic","MP":"bhopal","india":"delhi"}
# d={}
# for i in (a,b):
#     d.update(i)
# print(d)

i=1
d=[]
while i<=11:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j=j+1
 
    if count==2:
      d.append(i)
    i=i+1
print(d)
c={}
m=0
for i in d:
    c.update({i:m})
    m+=1
print(c)

