#Simulating L&L Course on Theoretical Physics: Classical Mechanics Problem 1.1
import numpy as np
import matplotlib.pyplot as plt

# Var
l1 = 2
l2 = 2
g = 9.8
m1 = 1
m2 = 1


# Function

def dub_pen(theta1_i, theta2_i, ang_vel1_i, ang_vel2_i, tot_time, tau=0.05):
    time_vec = [0]*tot_time
    theta1_vec = [0]*tot_time
    ang_vel1_vec = [0]*tot_time
    theta2_vec = [0]*tot_time
    ang_vel2_vec = [0]*tot_time
    
    theta1 = theta1_i
    ang_vel1 = ang_vel1_i
    
    theta2 = theta2_i
    ang_vel2 = ang_vel2_i
    
    for i in range(0, tot_time):
        ang_vel1_old = ang_vel1
        theta1_old = theta1
        ang_vel2_old = ang_vel2
        theta2_old = theta2
        
        ang_vel1 = ang_vel1_old+((((m2*g*np.sin(theta2_old)*np.cos(theta1_old-theta2_old))-
                                 (m2*np.sin(theta1_old-theta2_old)*((l1*(ang_vel1_old**2)*np.cos(theta1_old-theta2_old))+l2*(ang_vel2_old**2)))
                                 -((m1+m2)*g*np.sin(theta1_old)))/(l1*(m1+(m2*(np.sin(theta1_old-theta2_old)**2)))))*tau)
        ang_vel2 = ang_vel2_old+(((((m1+m2)*(l1*(ang_vel1_old**2)*np.sin(theta1_old-theta2_old)-
                                           g*np.sin(theta2_old)+g*np.sin(theta1_old)*np.cos(theta1_old-theta2_old)))
                                 +(m2*l2*(ang_vel2_old**2)*np.sin(theta1_old-theta2_old)*np.cos(theta1_old-theta2_old)))/(l2*(m1+(m2*(np.sin(theta1_old-theta2_old)**2)))))*tau)
        
        theta1 = theta1_old + (ang_vel1_old * tau)
        theta2 = theta2_old + (ang_vel2_old * tau)
        
        time_vec[i] = i*tau
        theta1_vec[i] = theta1
        theta2_vec[i] = theta2
        ang_vel1_vec[i] = ang_vel1
        ang_vel2_vec[i] = ang_vel2
    return [time_vec, theta1_vec, theta2_vec, ang_vel1_vec, ang_vel2_vec]

pendulum = dub_pen(np.pi/4, np.pi/3, 0, 0, 300)
print(pendulum[1])
plt.plot(pendulum[0],pendulum[1])
plt.plot(pendulum[0],pendulum[2])

# Sim
l = np.arange(0,300,1)

x1 = l1*np.sin(pendulum[1])
y1 = -l1*np.cos(pendulum[1])
x2 = x1 + (l2*np.sin(pendulum[2]))
y2 = y1 - (l2*np.cos(pendulum[2]))
# Division of trail
ns = 20
sec_per_trail = 2
for i in l:
    plt.figure()
    plt.plot(x1[i],y1[i],'bo',markersize=5)
    plt.plot([0,x1[i]],[0,y1[i]])
    plt.plot(x2[i],y2[i],'bo',markersize=5)
    plt.plot([x1[i],x2[i]],[y1[i],y2[i]])
    plt.xlim(-(l1+l2)-0.5,(l1+l2)+0.5)
    plt.ylim(-(l1+l2)-0.5,(l1+l2)+0.5)
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
        
        
    
         
            