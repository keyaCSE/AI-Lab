# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:19:41 2024

@author: USER
"""

dict={"fruit-1":"apple",
      "fruit-2":"banana",
      "fruit-3":"lichi"
      }

print(dict["fruit-1"])

for key in dict:
    print(key,dict[key])
    
dict["fruit-4"]="mango"

print(dict)

del(dict["fruit-1"])
element=dict.pop("fruit-2")
print(element)
print(dict)                                                                                                    