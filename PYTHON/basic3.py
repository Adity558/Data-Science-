# a =input("enter a number:-")
# print(a)
# b=input("enter b number;-")
# # print(a*b)
# print(type(a))
# print(type(b))


# # type casting 
# a=int(input("   "))
# b=int(input("enter b number:-"))
# print(a*b)


# lst= [1,2,3,4,5,6,67]
# print("ths is my list",lst)
# print("type of list, ", type(lst))
# tpl= tuple(lst)
# print("ths is my tuple",tpl)
# print("type of tuple;-",type(tpl))



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_set= {1,2,3,4,5,6,6,7,"jai"}
print('this is my set',my_set)
print("type of my set",type(my_set))
print("length of my set ",len(my_set))
# print(my_set[0])  # error because set is not indexable

lst=list(my_set)

print(lst)  # convert set to list

## some set operation

set1={1,2,3,4,5}
set2={4,5,6,7}

print("union od two sets are-:",set1.union(set2))
print("intersaction of two set",set1.intersection(set2))
print("difference off two set:- ",set1.difference(set2))
