"q1"
# details={"name":"monika","last_name":"jaiswal","age":21,"email":"monikajaiswal@navgurukul.org",}
# print(details["name"])
# print(details["last_name"])
# print(details["email"])
# print(details["age"])

"q2"
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1:
#     sum=sum+dict1[i]
# print(sum)

"q3"
# dict={}
# for i in range(1,16):
#     dict[i]=i*i
# print(dict,end=" ")

"q4"
# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)

"q5"
# d ={"fantasy": "harrypotter","romance": "me before you","fiction": "divergent"}
# for i in d.iteritems():
#     print(i)
# print(d.items())
# print(d.dict.iteritems()) 

# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
my_dict={"name":["monika",21,"coding"],"age":["shivani",22,"python"],"subject":["swati",22,"list"]}
print(*list(my_dict.keys()))
a=(list(my_dict.values()))
for i in range(len(a)):
    print(*(a[i]))