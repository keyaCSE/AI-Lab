# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:11:49 2024

@author: USER
"""

l=[1,2,3,4,5,6]
print(l[-5])
l.append(45)
print(l)
#l.reverse()
#print(l)

li=["keya","apra","elmi","mim"]
print(li)
li.append("sawda")
print(li)
li.reverse()
print(li)

l.insert(4,77)
print(len(l)) #koyta element ache
l[2:5]=[7,8,9]
print(l)

for i in l:
    print("the item is ", i)
l.remove(45)
print(l)
element=l.pop()
print(element)
print(l)
l.pop(2)
print(l)

#make new list
"""for i in l:
    i=i**3
    l.append(i)"""
    
new_l=[x**3 for x in l]

for i  in  new_l:
    print("the element in new_l ", i)
new_l.sort()
for i in new_l:
    print("the element in new _l sorted ", i)


    