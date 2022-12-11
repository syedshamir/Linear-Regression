# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-20, 20])
ax.set_ylim([-40, 50])
x_point=[]
y_point=[]

def onclick(event):
    if event.button is MouseButton.LEFT:
        print('button '+ str(event.button), 'x '+str(event.x), 'y '+str(event.y), 'xdata '+ str(event.xdata),
              'ydata '+ str(event.ydata))
        type(event.xdata)
        type(event.ydata)
        
        x_point.append(event.xdata)
        y_point.append(event.ydata)
        plt.plot(x_point, y_point,'bo')
        
        
    elif event.button is MouseButton.RIGHT:
        
        def my_linfit (x,y):
            n=len(x)
            x1=(sum(x))*(sum(x))
            x2=sum(np.square(x))
            x3=sum((x*y))
            x4=sum(x)
            
            y1=sum(y)
            
            #a = ((n*(x3))-((x3)*(y1))/(-(x1)+(n*(x2))))
            #b = (((y1)/n)-(a*(x4/n)))
            
            b = (((x1*y1)-(x2*y1))/(x1-(n*x2)))
            a = (-(n*(x3))+(x3))/((x1)-(n*(x2)))
            return a,b
        
        
        print('disconnecting callback')
        #plt.plot(x_point, y_point)
        print("clicked X Coordinated are" + str(x_point))
        print("clicked Y Coordinated are" + str(y_point))   
        print(type(x_point))
        print(type(y_point))
        x_arr=np.array(x_point)
        y_arr=np.array(y_point)    
        print(type(x_arr))
        print(type(y_arr))
        a,b= my_linfit(x_arr,y_arr)
        print(a,b)
        print(type(a))
        print(type(b))
        a=int(a)
        b=int(b)
        
        plt.plot(x_arr, a*x_arr+b, color='RED')
        #plt.plot(x_arr, y_arr,'bo')
        plt.axis([-20,20,-40,50])
        plt.disconnect(cid)
        fig.canvas.draw()
        
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()


"""
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)


def on_move(event):
    # get the x and y pixel coords
    x, y = event.x, event.y
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        print('data coords %f %f' % (event.xdata, event.ydata))


def on_click(event):
    if event.button is MouseButton.RIGHT:
        print('disconnecting callback')
        plt.disconnect(binding_id)


binding_id = plt.connect('motion_notify_event', on_move)
plt.connect('button_press_event', on_click)


plt.show()
"""
















