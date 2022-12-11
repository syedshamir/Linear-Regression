# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 20:59:52 2022

@author: HP
"""
# L inear s o l v e r
def my_linfit (x,y):
    n=len(x)
    x1=(sum(x))*(sum(x))
    x2=sum(np.square(x))
    x3=sum(x*y)
    x4=sum(x)
    y1=sum(y)
    
    #a = ((n*(x3))-(x3)*(y1))/(-(x1)+(n*(x2)))
    #b = (((y1)/n)-(a*(x4/n)))
    
    
    
    b = (((x1*y1)-((x2*y1)))/(x1-(n*x2)))
    
    a = (-(n*(x3))+(x3))/((x1)-(n*(x2)))
    return a,b
# Main
import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(-2,5,10)
y = np.random.uniform(0,3,10)
a,b= my_linfit (x,y)
print("A is"+ str(a))
print("B is"+ str(b))
plt.plot (x,y,'bo')

#xp = np.arange(-2 , 5 , 0.1)
#print(xp)
plt.plot(x, (a*x)+b, color='red')
plt.axis([-22,22,-40,55])
plt.show( )










