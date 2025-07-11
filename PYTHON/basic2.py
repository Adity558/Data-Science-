#,,,,,,,,,,,,,,,,,,,,,,,,,,,
#list
# lst= [1,2,3,4, 4,5,6,7, "rohit", 2.3]

# # properties of list

# # mutable
# # duplicated values
# # hetro -- diffrent types ke data types ko use kar sakta hee 
# # order

# # array
# # homogeneous
# # collection of similar types of data types 
# # array is faster the list approx 10 times 
# # array memory allocate karta hee


# print("my first list:-",lst)
# print("len of list:-",len(lst) )
# print("type of list",type(lst))


# print(lst[0])
# print(lst[2])

# print(lst[0:5])

# lst=[1, 2, 3, 4, 4, 5, 6, 7, 2.3]
# lst.pop---- used to poplast element
# print(lst)

# lst.append(100)--- used when to add new element at last
# print(lst)
# lst.insert(0,100)--- used to add element at specific position
# print(lst)

# copy_lst = lst.copy()
# print(copy_lst)

# lst.reverse()

# lst.remove(2.3)
# print(lst)

# lst.sort()
# print(lst)

# print(lst.count(4))

# lst.clear()----  used for clearing lst
# 
# 
# 
#  taskk---------------------------------------
# make a list and make list inside the list and need to acces no from inside list
# lst= [1,2,3,4,[5,6],7]
# print(lst[4][1])



# ############## tuples----------------------------------

# tpl=(1,2,3,4,5,"m","n")
# print("my first tuple:-",tpl)

# print("len of tuple:-",len(tpl) )
# print("type of tuple",type(tpl))

# print(tpl[0])
# print(tpl[2])
# print(tpl[0:4])
# # print(tpl[0:5:2])--- used to print element at specific index with
# # build

# a= 1,2,58,5,58,5,5,85,2
# print(a)
# print(type(a))
# print(len(a))

# this process is known as tuple unpacking 
# a, b, c =(1,2,3)
# print(a)
# print(b)
# print(c)

# a, b, c =1,2,3
# print(a)
# print(b)
# print(c)

# tuple unpacking

# a=1,2,3,4,5,67,56
# print(max(a))
# print(min(a))
# print(sum(a))



# #tuples dictionay-----------------------------------------
# d={"name":"mohit",
# "age":20,
# "city":"delhi",
# "marks":100
# }
# print(d)
# print("len of dictionary:-",len(d))
# print("type of dictionary:-",type(d))
# print(d['name'])
# print(d['age'])
# print(d['city'])
# print(d['marks'])

# # for changing and adding any new value in dictionary
# d['city']= "jaipur"
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

# d.copy()
# print(d.copy())

# d.clear()
# print(d)
d={"name":"mohit",
"age":20,
"city":"delhi",
"marks":100
}


d.update({"name ": "aditya"})
print(d)


my_dict = {'a': '1',
          'b': '2',
           'c':'3'}
print(my_dict)
## if key doesnot exit  default value found and get fuction is safer than swquare brakets 

print(my_dict.get('a'))
print(my_dict.get('b'))
print(my_dict.get('c'))
print(my_dict.get('d'))

### if key found then it will return value otherwise it will return none and  and its less safer then get it
## it show error if key not found
print(my_dict['a'])
print(my_dict['b'])
print(my_dict['c'])
# print(my_dict['d'])


