a=[]
for i in range(10):
    name=input("enter the name:-")
    num=int(input("enter the marks:-"))
    b=name,num
    a.append(b)
print(dict(a))
