"q1"
# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)

"q2"
# Expected Result : {0: 10, 1: 20, 2: 30}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic={}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i in (dic1,dic2,dic3):
#     dic.update(i)
# print(dic)

"q4"
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# def is_key_presant(x):
#     if x in d:
#         print(x,"is presant in dic")
#     else:
#         print(x,"is not presant in dic")
# is_key_presant(9)

"q5"
#output= x -> 10
# y -> 20
# z -> 30

# d = {'x': 10, 'y': 20, 'z': 30} 
# for i in d:
#     print(i,"->",d[i])

"q6"
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# n=int(input("enter the number"))
# dic={}
# for i in range(1,n+1):
#     dic[i]=i*i
# print(dic)

"q8"
# output={'x': 300, 'y': 200, 'a': 100, 'b': 200}
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d2.update(d1)
# print(d2)

"q9"
#output= Red corresponds to  1
# Green corresponds to  2
# Blue corresponds to  3

# d = {'Red': 1, 'Green': 2, 'Blue': 3} 
# for i in d:
#     print(i,"correspond",d[i])

"q10"
# output=293 
# my_dict = {'data1':100,'data2':-54,'data3':247}
# sum=0
# for i in my_dict:
#     sum+=my_dict[i]
# print(sum)

"q11"
# my_dict = {'data1':100,'data2':-54,'data3':247}
# mlty=1
# for i in my_dict:
#     mlty*=my_dict[i]
# print(mlty)

"q12"
#output= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# {'b': 2, 'c': 3, 'd': 4}

# myDict = {'a':1,'b':2,'c':3,'d':4}
# for i in (myDict):
#     a=myDict[i]
#     print(a)
# myDict.pop("a")
# print(myDict)

"q13"
# output={'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# a=dict(zip(keys,values))
# print(a)
# i=0
# b=0
# a=[]
# while i<len(keys):
#     c=keys[i],values[b]
#     a.append(c)
#     i+=1
#     b+=1
# print(dict(a))

"q14"
# output=black: #000000                                                                                                
# green: #008000                                                                                                
# red: #FF0000                                                                                                  
# white: #FFFFFF 

# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
# for i in sorted (color_dict):
#     print(i,color_dict[i])

"q15"
# output=Maximum Value:  5874                                                                                          
# Minimum Value:  500

# from multiprocessing.sharedctypes import Value
# from typing import Counter
# my_dict = {'x':500, 'y':5874, 'z': 560}
# max=0
# for i in my_dict:
#     if my_dict[i]>max:
#         max=my_dict[i]
# print(max)
# my_dict = {'x':500, 'y':5874, 'z': 560}
# a=min(my_dict.values())
# print("min value",a)


# for i in my_dict:
#     min=my_dict[i]
#     if my_dict[i]<min:
#         min=my_dict[i]
# print(min)


"q16"
# output={'x': 'red', 'y': 'Yellow', 'z': 'Green'}

# a={}
# for i in range(3):
#     n=input("enter the key")
#     m=input("enter the value")
#     a.update({n:m})
# print(a)

# def dic(n,m):
#     a={}
#     n=input("enter the key")
#     m=input("enter the value")
#     a.update({n:m})
#     print(a)
# for i in range(3):
#     dic(3,3)



"q17"
# output={'id2': {'subject_integration': ['english, math, science'], 'class': ['V'], 'name': ['David']}, 'id4': {'subje
# ct_integration': ['english', 'math', 'science'], 'class': ['V'], 'name': ['Surya']}, 'id1': {'subject_integration'
# : ['english, math, science'], 'class': ['V'], 'name': ['Sara']}} 


# student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 
#     'subject_integration': ['english, math, science']},'id2': {'name': ['David'], 
#     'class': ['V'], 'subject_integration': ['english, math, science']},
#  'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']
#    },'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']
#    },
# }
# print(student_data)
# result = {}

# for k,v in student_data:
#     if v not in result:
#         result[k] = v

# print(result)

# "q19"
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# d={}
# for i in d1,d2:
#     d.update(i)
# for i in d:
#     if i in d2:
#         if i in d1:
#             d.update({i:d2[i]+d1[i]})
# print(d)

"q20""remove duplicate value"
# data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# c=[]
# for k in data:
#     for i in k:
#         if k[i] not in c:
#             c.append(k[i])
# print(c)

"remove duplicate keys"
# data= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# c=[]
# for k in data:
#     for i in k:
#         if i not in c:
#             c.append(i)
# print(c)

'"q21"'
# Expected Output:
# ac
# ad
# bc
# bd
# sample_data = {'1':['a','b'], '2':['c','d']}
# for i in sample_data["1"]:
#     for j in sample_data["2"]:
#         r=i+j
#         print(r)

# data = {'1':['a','b'], '2':['c','d']}
# for i in (data["1"]):
#     for j in (data["2"]):
#         print(i+j)

"q22"
# from typing import Counter
# a = [1,2,3,2,3,4,5,5,6]
# c=Counter(a)
# print(c)

# a = [1,2,3,2,3,4,5,5,6]
# b=[]
# d=0
# for i in a:
#     n=[]
#     for j in (a):
#         if i==j:
#             d+=1
#     n.append()
    
# print(b,d)

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
# m=Counter(my_dict)
# s=m.most_common(3)
# for i in s:
#     print(i[0])

# d="w3resorces"
# b={}
# for i in d:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)
"q23"
# my_dict = [
# {'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}]
# d = {}
# for x in my_dict :
#     if x['item'] not in d :
#         d.update({x['item'] : x['amount']})
#     else :
#         d[x['item']] += x['amount']
#     print(d)

"q25"
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in my_dict:
#     a= my_dict[{"C1"[i],"C2"[i],"C3"[i]}]
# print(a)

"q26"
# d = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# s=0
# s1=0
# for i in d:
#     s+=i['id']
#     s1+=i['success']
# print(s)
# print(s1)

# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))
"q27"
# list=[1,2,3,4]
# n=dict={}
# for i in list:
# {    dict[i] = {}
#     dict=dict[i]
# print(n)
"q28"
# l = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# # l=[1,7,6,8,9,5,4,3]
# for i in range(len(l)):
#     for j in  range(i+1,len(l)):
#         if l[i]>=l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# 
# l = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# for i in l:
#     l[i]=sorted(l[i])
# print(l)

"q29"
# courses = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
# clean_dic = {}
# for a,b in courses.items():
#     a = a.split()
#     clean_dic["".join(a)] = b
# print(clean_dic)


# c={}
# for i in courses:
#     if " " in courses:
#         courses[i].remove( )
#     print(courses,i)

"q30"
# from typing import Counter
# sample_data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# a=Counter(sample_data)
# h=a.most_common(3)
# for i in h:
#     print(i[0],":",i[1],"")

"q31"
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key   value   count")
# c=0
# for i in dict_num:
#     c+=1
#     print(i,"\t",dict_num[i],"\t",c)

"q32"
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])

"q33"
# student = {'name': 'Alex','class': 'V','roll_id': '2'}
# if 'name' and 'class' in student.keys():
#     print("exist")
# else:
#     print("noy exist")

# student = {'name': 'Alex', 'class': 'V', 'roll_id': 2}
# count = len(student.keys())
# if count > 1:
#     print(True)
# else:
#     print(False)

# "q34"
# # from typing import Counter
# l = {'Math':81, 'Physics':83, 'Chemistry':87}
# print(l[-1::-1])

# a=Counter(l)
# print(a.most_common(3))

"q36"
# list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# list2 = [1, 2, 2, 3]
# dic = {}
# for i in range(len(list1)):
#     if list1[i] not in dic:
#         dic.update({list1[i]: {list2[i]}})
# print(dic)

"q37"
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
# for d in student_details:
#     d['V+VI'] = ((d.pop('V') + d.pop('VI'))/2)
# print(student_details)

# for i in student_details:
#     n1=i['V']
#     n2=i['VI']
#     i['V'+'VI']=(n1+n2)//2
# print(student_details)

# "q38"
# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for i,j in y.items():
#     if  x[i]==y[i]:
#         print(i,'.',j,'presant in x,y both' )
"q40"
# dic_list= {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#  'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#  'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# print(dic_list['x'][4])
# print(dic_list["y"][4])
# print(dic_list["z"][4])

"q41"
# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3':None}
# d={}
# for i,j in dict1.items():
#     if j!= None:
#         d[i]=j
# print(d)
"q42"
# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# a={}
# for i,j in marks.items():
#     if j>170:
#         a[i]=j
# print(a)

# for i in marks:
#     if marks[i]>170:
#         print({i,marks[i]})
        

"q43"
# stu_id = ["S001", "S002", "S003", "S004"] 
# stu_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
# stu_grade = [85, 98, 89, 92]
# d=[]
# d1=[]
# for i in range(len(stu_name)):
#     dic={}
#     for j in range(len(stu_name)):
#         if i ==j:
#             dic=({stu_name[i]:stu_grade[j]})
#             d.append(dic)
# for k in range(len(stu_id)):
#     dic1={}
#     dic1=({stu_id[k]:d[k]})
#     d1.append(dic1)
# print(d1)   
           

# l1 = ['S001', 'S002', 'S003', 'S004']
# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3 = [85, 98, 89, 92]
# l5 =[]
# l6 = []
# for i in range(len(l2)):
#     d2 = {}
#     for j in range(len(l3)):
#         if i == j:
#             d2=({l2[i]:l3[j]})
#             l5.append(d2)
# for x in range(len(l1)):
#     d3 = {}
#     d3=({l1[x]:l5[x]})
#     l6.append(d3)
# print(l6)

"44"
# students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 
# 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# for i,j in students.items():
#     if j[0]>=6.0 and j[1]>=70:
#         a=i
#         b={a:(students[i])}
# print(b)

"q45"
# n=int(input("enter the number"))
# students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# for i in students.values():
#     if i==n:
#         print("true",n)
#     else:
#         print("false",n)
#     break

"q46"
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# a={}
# for i,j in colors:
#     a.setdefault(i, []).append(j)
# print(a)

# L = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {}
# for i in L:
#     if i[0] not in d:
#         d.update({i[0]:[i[1]]})
#     else:
#         d[i[0]].append(i[1])
# print(d)

"q47"
# marks = {'science': [88, 89, 62, 95], 'language': [77, 78, 84, 80]}
# a=marks['science']
# b=marks["language"]
# d=[]
# for i in range(len(a)):
#     c={}
#     for j,k in marks.items():
#         c.update({j:k[i]})
#     d.append(c)
# print(d)


"q48"
# colors = [{"id" : "#FF0000", "color" : "Red"}, 
#           {"id" : "#800000", "color" : "Maroon"}, 
#           {"id" : "#FFFF00", "color" : "Yellow"}, 
#           {"id" : "#808000", "color" : "Olive"}] 
# d=[]
# for i in colors:
#     if i["id"]!="#FF0000":
#         d.append(i)
# print(d)

"q49"
# l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]

"q50"
# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for i in (a):
#     a[i].clear()
# print(a)

"q51"
# dic={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# d=[]
# c=[]
# b=[]
# for i in dic["Math"]:
#     d.append(i+1)
# for i in dic["Physics"]:
#     c.append(i-2)
# for i in dic["Chemistry"]:
#     b.append(i)
# l={"Math":d}
# m={"Physics":c}
# n={"Chemistry":b}
# o=l,m,n
# print(o)

"q52"
# a=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# b=[]
# c=[]
# for i in a:
#     c.append(i['Math'])
#     b.append(i['Science'])
# print(["Science =",b])
# print(["Math =",c])

"q53""1st type"
# dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# d={}
# for i,j in dic.items():
#     d.update({j:len(j)})
# print(d)

"2nd type"
# dic={'1':'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# d={}
# for i in dic.values():
#     d[i]=len(i)
# print(d)

"q55"
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# for i in num:
#     print(i)

"q56"
# color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# a=[]
# for i,j in color_dict.items():
#     b=[i,j]
#     a.append(b)
# print(a)

# a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# b=[]
# for i in a:
#     c=[i,(a[i])]
#     b.append(c)
# print(b)

"q57"
# dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# d={}
# for i,j in dic.items():
#     c=[]
#     for k in j:
#         if k%2==0:
#             c.append(k)
#         d.update({i:c})
# print(d)

# a={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# d={}
# for i,j in a.items():
#     c=[]
#     for k in j:
#         if k%2==0:
#             c.append(k)
#         d.update({i:c})
# print(d)

"q58"
# from itertools import combinations
# com_dic = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# lis=[]
# for i in range(1,len(com_dic)):
#     for x in combinations(com_dic,i):
#         dic={z:com_dic[z] for z in x}
#         lis.append(dic)
# print (lis)            

"q59"
# from heapq import nlargest
# test_dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# n=int(input("entder the number"))
# r=nlargest(n,test_dic,key=test_dic.get)
# print("the top N value pair:",(r))

"q60"
# dictt = {'V': [10, 12],'VI': [10],'VII': [10, 20, 30, 40],'VIII': [20],
# 'IX': [10,30,50,70],'X': [80]}
# m=1
# d=[]
# for i ,j in dictt.items():
#     if len(j)==m:
#         d.append(i)
# print(d)

"q61"
# dictt = {'V': 10,'VI': 10,'VII': 40,'VIII': 20,'IX': 70,'X': 80,'XI': 40,'XII': 20, }
# d={}
# for i,j in dictt.items():
#     if j in d:
#         d[j]+=1
#     else:
#         d[j]=1
# print(d)

"q62"
# def test(dict,keys):
#     a=[]
#     for i in dict:
#         for j in keys:
#             a.append(i[j])
#     return a
# "2nd type"
# def test(dictt,keys):
#     return [list(d[k] for k in keys) for d in dictt] 

# students = [
#         {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#         {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#         {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#         {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#         {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
#         ]
# print("\n",test(students,('student_id', 'name')))
# print("\n",test(students,('name','class')))
# print("\n",test(students,('student_id','name','class')))

"q63"
# def test(lst):
#     result = {item[0]: item[1:] for item in lst}
#     return result
# students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'],
# [4, 'Lynne''Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# print(test(students))

# "2nd type"
# students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'],
# [4, 'Lynne''Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# d={}
# for i in students:
#     d.update({i[0]: i[1:]})
# print(d)

"q64"

# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 
# 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# print({k: v[0] for k, v in a.items()})
# res=[]
# for i,j in a.items():
#     for k in j:
#         res.append(i:j[k])
# print(res)


'q65'
# d={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# a=0
# for i in d.values():
#     a+=len(i)
# print(a)

"q66"
# id=input("enter the keyname:-")
# d=input("enter the value:-")
# students = [
#         {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#         {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#         {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#         {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#         {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
#         ]
# for i in students:
#     for j in i:
#         if id[j]==d[i[j]]:
#             print(True)
#         else:
#             print(False)
"q66"
# def demo(dictt,key,value):
#     if any(i[key]==value for i in dictt):
#         return True
#     return False
# students = [
#         {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#         {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#         {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#         {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#         {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# print(demo(students,'student_id',1))
# print(demo(students,'name','Jean Castro'))
# print(demo(students,'student_id',6))

"q67"
# students = {'Ora Mckinney': 8,'Theodore Hollandl': 7,'Mae Fleming': 7,
# 'Mathew Gilbert': 8,'Ivan Little': 7,"monika":9}
# d2 = {}
# for k,v in students.items():
#     d2.setdefault(v,[]).append(k)
# print(d2)

"q68"
# a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# b={'x': 300, 'y': 'Red', 'z': 600}
# for i in a:
#     if i in b:
#         a[i]=[a[i],b[i]]
#     else:
#         a[i]=[a[i]]
# print(a)


# from collections import defaultdict
# def demo(*dicct):
#     r=defaultdict(list)
#     for i in dicct:
#         for j in i:
#             r[j].append(i[j])
#     return dict (r)
# a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# b={'x': 300, 'y': 'Red', 'z': 600}
# print(demo(a,b))


"q69"
# from collections import defaultdict
# from math import floor
# def test(lst,fnc):
#     d=defaultdict(list)
#     for i in lst:
#         d[fnc(i)].append(i)
#     return dict(d)
# nums = [7,23, 3.2, 3.3, 8.4,8.8]
# print(test(nums,floor))

# from collections import defaultdict
# def test(lst,fnc):
#     d=defaultdict(list)
#     for i in lst:
#         d[fnc(i)].append(i)
#     return dict(d)
# color=['Red', 'Green', 'Black', 'White', 'Pink']
# print(test(color,len))

# from collections import defaultdict
# color=['Red', 'Green', 'Black', 'White', 'Pink']
# d=list,[]
# for i in color:
#     d[len(i)].append(i)
# print(dict(d))

"q70"
# a=[1,2,3,4]
# b={}
# for i in a:
#     b.update({i:i**2})
# print(b)

"q71"
# users = {'Carla ': {'name': {'first': 'Carla ','last': 'Russell' },
# 'postIds': [1, 2, 3, 4, 5]}}
# d={}
# for i in users:
#     for j in users[i]:
#         for k in users[i][j]:
#                 print(k)

"q72"
# output={10: 'Theodore', 11: 'Mathew', 9: 'Roxanne'}
# students = {'Theodore': 10,'Mathew': 11,'Roxanne': 9,}
# d={}
# for i in students:
#     d.update({students[i]:i})
# print(d)

"q73"
# output=[18, 22, 20, 18]
# lst=[{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, 
# {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# a=[]
# for i in lst:
#     a.append(i['age'])
# print(a)

"q74"
# output={'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}
# dicc={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': 
# {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# d={}
# for i in dicc:
#     for j in dicc[i]:
#         d.update({i:dicc[i][j]})
# print(d)

"q75"
# output=['Roxanne', 'Betty']
# n=int(input("enter the chek sem value number"))
# d={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20,"monika":21}
# a=[]
# for i in d:
#     if d[i]==n:
#         a.append(i)
# print(a)
# c=(a[1:4:2])
# print(c)
    
"q76"
# output={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# def cambin(keys,value):
#     return dict(zip(keys,value))
# d1=['a', 'b', 'c', 'd', 'e', 'f']
# d2=[1, 2, 3, 4, 5]
# print(cambin(d1,d2))


# i=0
# a=[]
# b=0
# d=str(d2)
# while i<len(d1):
#     c=d1[i],d[b]
#     # a.append(c)
#     i+=1
#     b+=1
# print(c)


"q77"
# output=[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]
# d1={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# d=[]
# for i,j in d1.items():
#     k=(i,j)
#     d.append(k)
# print(d)

"q78"
# output=['Theodore', 'Roxanne', 'Mathew', 'Betty']
# dict={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# d=[]
# for i in dict:
#     d.append(i)
# print(d)

"q79"
#output= [19, 20, 21, 20]
# dic={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# d=[]
# for i in dic:
#     d.append(dic[i])
# print(d)

# "q80"
# #output= ('Roxanne', 'Theodore')
# a={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# max=0
# for i in (a):
#     if a[i]>max:
#         c=i
#     max=a[i]
# print(c)

# "logical q"
# a=["a","b","c"]
# b=["d","e","f"]
# c=["g","h","i"]
# d={}
# for i in a:
#     d.update({i:{b[i]:c[i]}})
# print(d)

# n=int(input("enter the number"))
# a={}
# for i in range(n):
#     name=input("enter name")
#     age=int(input("enter the age"))
#     a.update({name:age})
# print(a)


# a=["a","b","c","d","e"]
# b=["f","g","h","i","j"]
# d={}
# i=0
# while i<len(a):
#     c=a[i]+b[-i]
#     d.update({i:c})
#     i+=1
# print(d)

    # a.append(n)
# print(a)
# m=0
# j=0
# while j<len(a):
#     if a[j]>m:
#         m=a[j]
#     j+=1
# print(m)
