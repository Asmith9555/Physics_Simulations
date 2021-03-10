# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:48:45 2020

@author: smith
"""
#Simulating L&L Course on Theoretical Physics: Classical Mechanics Problem 1.1
import numpy as np
import matplotlib.pyplot as plt

# Var
L = 5
g = 9.8


# Data
def sim_pendulum(theta_init,ang_vel_init,total_time,tau=0.2):
    time_vec = [0]*total_time
    theta_vec = [0]*total_time
    ang_vel_vec = [0]*total_time
    
    theta = theta_init
    ang_vel = ang_vel_init
    
    for i in range(0,total_time):
        #establishing relative initial cond.
        ang_vel_old = ang_vel
        theta_old = theta
        
        #Updating Values
        ang_vel = ang_vel_old - ((g/L)*np.sin(theta_old))*tau
        theta = theta_old + ang_vel*tau
        
        #Record Values
        time_vec[i] = i*tau
        theta_vec[i] = theta
        ang_vel_vec[i] = ang_vel
    return [time_vec,theta_vec,ang_vel_vec]

pendulum = sim_pendulum(np.pi/4, 0, 500)
plt.plot(pendulum[0],pendulum[1])
plt.plot(pendulum[0],pendulum[2])
plt.show()

# Sim
l = np.arange(0,250,1)

x = L*np.sin(pendulum[1])
y = -L*np.cos(pendulum[1])

for i in l:
    plt.figure()
    plt.plot(x[i],y[i],'bo',markersize=15)
    plt.plot([0,x[i]],[0,y[i]])
    plt.xlim(-L-0.5,L+0.5)
    plt.ylim(-L-0.5,L+0.5)
    