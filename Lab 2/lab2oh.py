import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(1,figsize=(6,6))
fig.clf()
axes = [fig.add_subplot(321),\
        fig.add_subplot(322),\
        fig.add_subplot(323),\
        fig.add_subplot(324),\
        fig.add_subplot(325),\
        fig.add_subplot(326)]

# You can use axes[0], axes[1], ....  axes[5] to make the six histograms.

# Your code goes here

data = np.loadtxt('refractionData.txt', skiprows = 3)

axes[0].hist(data[0], range = (-10, 50), bins = 15)
axes[0].set_xlabel('beta (deg.)')
axes[0].set_xticks([-10, 0, 10, 20, 30, 40, 50])
axes[0].set_title('alpha = 10 deg.')

axes[1].hist(data[1], range = (-10, 50), bins = 15)
axes[1].set_xlabel('beta (deg.)')
axes[1].set_xticks([-10, 0, 10, 20, 30, 40 , 50])
axes[1].set_title('alpha = 20 deg.')

axes[2].hist(data[2], range = (-10, 50), bins = 15)
axes[2].set_xlabel('beta (deg.)')
axes[2].set_xticks([-10, 0, 10, 20, 30, 40, 50])
axes[2].set_title('alpha = 20 deg.')

axes[3].hist(data[3], range = (-10, 50), bins = 15)
axes[3].set_xlabel('beta (deg.)')
axes[3].set_xticks([-10, 0, 10, 20, 30, 40, 50])
axes[3].set_title('alpha = 30 deg.')

axes[4].hist(data[4], range = (-10, 50), bins = 15)
axes[4].set_xlabel('beta (deg.)')
axes[4].set_xticks([-10, 0, 10, 20, 30, 40, 50])
axes[4].set_title('alpha = 40 deg.')

axes[5].hist(data[5], range = (-10, 50), bins = 15)
axes[5].set_xlabel('beta (deg.)')
axes[5].set_xticks([-10, 0, 10, 20, 30, 40, 50])
axes[5].set_title([-10, 0, 10, 20, 30, 40, 50])

#%%

# Part 2 - Table of measurements

# Your code goes here

a0 = np.zeros(len(data[0]))
a1 = np.zeros(len(data[1]))
a2 = np.zeros(len(data[2]))
a3 = np.zeros(len(data[3]))
a4 = np.zeros(len(data[4]))
a5 = np.zeros(len(data[5]))

for i in range((len(data[0]))):
    a0[i] = np.radians(data[0][i])
    a1[i] = np.radians(data[1][i])
    a2[i] = np.radians(data[2][i])
    a3[i] = np.radians(data[3][i])
    a4[i] = np.radians(data[4][i])
    a5[i] = np.radians(data[5][i])
    
avg0 = np.mean(a0)
avg1 = np.mean(a1)
avg2 = np.mean(a2)
avg3 = np.mean(a3)
avg4 = np.mean(a4)
avg5 = np.mean(a5)

stdev0 = np.std(a0)
stdev1 = np.std(a1)
stdev2 = np.std(a2)
stdev3 = np.std(a3)
stdev4 = np.std(a4)
stdev5 = np.std(a5)

sine0 = np.sin(avg0)
sine1 = np.sin(avg1)
sine2 = np.sin(avg2)
sine3 = np.sin(avg3)
sine4 = np.sin(avg4)
sine5 = np.sin(avg5)

s0 = np.sin(stdev0)
s1 = np.sin(stdev1)
s2 = np.sin(stdev2)
s3 = np.sin(stdev3)
s4 = np.sin(stdev4)
s5 = np.sin(stdev5)

print('|', '10 |', np.sin(np.radians(10)), '|', avg0, '|', np.sin(avg0), '|', s0, '|')
print('|', '20 |', np.sin(np.radians(20)), '|', avg1, '|', np.sin(avg1), '|', s1, '|')
print('|', '30 |', np.sin(np.radians(30)), '|', avg2, '|', np.sin(avg2), '|', s2, '|')
print('|', '40 |', np.sin(np.radians(40)), '|', avg3, '|', np.sin(avg3), '|', s3, '|')
print('|', '50 |', np.sin(np.radians(50)), '|', avg4, '|', np.sin(avg4), '|', s4, '|')
print('|', '60 |', np.sin(np.radians(60)), '|', avg5, '|', np.sin(avg5), '|', s5, '|')








#%%

# Part 3 - Snells law plot and fit

fig = plt.figure(2,figsize=(6,6))
fig.clf()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# You can use ax1 and ax2 for the Snell's law plot and the chi squared plot.

# Your code goes here

# Part 4 - Chi squared plot

# Your code goes here





######################################################
