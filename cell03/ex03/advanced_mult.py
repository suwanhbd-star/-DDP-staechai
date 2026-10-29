#!/usr/bin/env python3
a = 0
while a < 11 :
    x = 0
    result = " "
    while x < 11 :
      result += str(x*a)+" "
      x += 1 
      
    print(f"Table de {a},:{result}")
    a += 1