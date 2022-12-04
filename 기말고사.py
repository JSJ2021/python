# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:48:20 2022

@author: user
"""

class Cat:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
    
    def __str__(self):
        a = (f"{self.name} + {self.age}")
        return a
        
missy = Cat('Missy',3)
print(missy)

class Roket:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    
    
    def __str__(self):
        a = (f"{self.x} {self.y}")
        return a
    def moveup(self):
        self.y += 1
        
myroket = Roket()
print("로켓의 높이",myroket.y)

myroket.moveup()

print("로켓의 높이",myroket.y)





class Box:
    
    def __init__(self,l,h,d):
        self.length = l
        self.height = h
        self.depth = d
        
    def __str__(self):
        return  f"({self.length},{self.height},{self.depth})"
    
    def getH(self):
        return self.height
    def getL(self):
        return self.length
    def getD(self):
        return self.depth
        
b1= Box(100,100,100)
print(b1)

print("상자의 크기는",b1.depth*b1.height*b1.length)

print("상자의 크기는",b1.getD()*b1.getH()*b1.getL())



class Rect:
    
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    
    
    def overlep(self,r):
        if (self.x + self.width >= r.x ) and (self.y + self.height >= r.y) :
            return True 
        else :
            return False
        
        
r1 = Rect(0, 0, 100, 100)
r2 = Rect(10, 10, 100, 100)
r1.overlep(r2)






