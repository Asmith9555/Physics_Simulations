# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:37:05 2021

@author: ā
"""

import numpy as np
import matplotlib.pyplot as plt

# Var
l = 5
g = 9.8
a = 5

# Data
def sim_pendulum(phi_i,ang_vel_i,theta_i,tot_time,tau=0.1):
    time_vec = [0]*tot_time
    phi_vec = [0]*tot_time
    ang_vel_vec = [0]*tot_time
    # Vector for fixed assembly
    theta_vec = [0]*tot_time
    
    phi = phi_i
    theta = theta_i
    ang_vel = ang_vel_i
    
    for i in range(0,tot_time):
        #establishing relative initial cond.
        ang_vel_old = ang_vel
        theta_old = theta
        phi_old = phi
        
        #Updating Values
        ang_vel = ang_vel_old + (((a/l)*(((np.pi/30)/tau)**2)*np.cos(phi_old-theta_old))-((g/l)*np.sin(phi_old)))*tau
        phi = phi_old + (ang_vel*tau)
        theta = theta_old - (np.pi/30)
        
        #Record Value
        time_vec[i] = i*tau
        phi_vec[i] = phi
        theta_vec[i] = theta
        ang_vel_vec[i] = ang_vel
    return [time_vec,phi_vec,theta_vec,ang_vel_vec]

pendulum = sim_pendulum(np.pi/4, np.pi/2, 0, 500)
plt.plot(pendulum[0],pendulum[1])
plt.plot(pendulum[0],pendulum[2])
plt.show()

# Sim
tot_time = np.arange(0,500)

x1 = a*np.sin(pendulum[2])
y1 = -a*np.cos(pendulum[2])
x2 = a*np.sin(pendulum[2]) + l*np.sin(pendulum[1])
y2 = -a*np.cos(pendulum[2])- l*np.cos(pendulum[1])

# Division of trail
ns = 20
sec_per_trail = 1
for i in tot_time:
    plt.figure()
    plt.plot(x1[i],y1[i],'bo',markersize=5)
    plt.plot(x2[i],y2[i],'bo',markersize=5)
    plt.plot([x1[i],x2[i]],[y1[i],y2[i]])
    plt.xlim(-(a+l)-0.5,(a+l)+0.5)
    plt.ylim(-(a+l)-0.5,(a+l)+0.5)
    plt.Circle((0,0), 2, color = "orange")
    for j in range(ns):
        tau = 0.05
        max_trail = int(sec_per_trail/tau)
        s = max_trail // ns
        imin = i - (ns-j)*s
        if imin < 0:
            continue
        imax = imin + s + 1
        # The fading looks better if we square the fractional length along the
        # trail.
        alpha = (j/ns)**2
        plt.plot(x2[imin:imax], y2[imin:imax], c='r', solid_capstyle='butt',
                lw=2, alpha=alpha)
