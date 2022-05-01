# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:43:19 2021

@author: john
"""

from random import choice


class randomWalk:
    
    def __init__(self,num_points=6000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction=choice([1,-1])
            y_distance=choice([1,2,3,4])
            y_step = y_direction * y_distance
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
            
            
import matplotlib.pyplot as p

rw =  randomWalk()
rw.fill_walk()           
p.style.use('dark_background')
fig, ax = p.subplots()            
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=p.cm.Blues, edgecolors='none', s=15)
ax.scatter(0,0,c="green",edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],
            rw.y_values[-1], c='red',edgecolors='none',s=100)
p.show()
p.savefig('随机图',bbox_inches='tight')            