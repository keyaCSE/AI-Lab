# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 02:45:09 2024

@author: USER
"""

g={
   5:[6,7],
   6:[8,9],
   7:[10,11],
   8:[12],
   9:[],
   10:[],
   11:[],
   12:[]
   }

v=[]
q=[]

def bfsAlgo(v,g,root,q):
    v.append(root)
    q.append(root)
    
    while q:
        value=q.pop(0)
        print(value,end=" ")
        for x in g[value]:
            if x  not in v:
                v.append(x)
                q.append(x)
                
bfsAlgo(v,g,5,q)
                
    