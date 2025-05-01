# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 08:09:04 2024

@author: USER
"""

a=33
b=200
if b>a:
    print("b is greater than a")
#elif   
A=40
B=33

if B>A:
    print("B is greater than A")
elif B==A:
    print("A and B are equal")
    C=A+B
    print(C)
else:
    print("A is greater than B")

#same line for one statement
aa=700
bb=500
print("A") if aa>bb else print("B") 

#more than one condition
p=200
q=33
r=500
if p>q and r>p:
    print("Both condition are true")
P=200
Q=33
R=500
if P>Q or P>R:
    print("At least one condition is true")
PP=33
QQ=200
if not PP>QQ:
    print("A is not greater")

#Nested
x=41

if x>10:
    print("Greater than 10")
    if x>20:
        print("Greater than 20")
    else:
        print("Lesser than 20")
        
fruits = ["apple", "banana", "cherry"]
for o in fruits:
    print(o)
    
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for k in adj:
  for l in fruits:
    print(k, l)