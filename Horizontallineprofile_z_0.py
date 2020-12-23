# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 00:40:44 2020

@author: MG
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
# import math
# import matplotlib.mlab as ml

os.chdir("/Users/MG/Dropbox/0. Research/2. Tribocharge nanopatterning/Electrostatic Simulation/11152020-")

# rv_data_d05 = pd.read_csv('PotentialandEfield(z=0)_0.2500.csv'); 
# rv_data_d5 = pd.read_csv('PotentialandEfield(z=0)_0.1000.csv'); 
# rv_data_d50 = pd.read_csv('d50nm_z0_flat.csv'); 
rv_data_d50_dip = pd.read_csv('d50nm_z0_dipwithair.csv'); 
rv_data_d1_dip = pd.read_csv('d1nm_z0_dipwithair.csv'); 
rv_data_d5_dip = pd.read_csv('d5nm_z0_dipwithair.csv'); 
rv_data_d25_dip = pd.read_csv('d25nm_z0_dipwithair.csv'); 


# r50 = rv_data_d50.iloc[:,0]; p50 = rv_data_d50.iloc[:,1]
r50dip = rv_data_d50_dip.iloc[:,0]; p50dip = rv_data_d50_dip.iloc[:,1]
r1dip = rv_data_d1_dip.iloc[:,0]; p1dip = rv_data_d1_dip.iloc[:,1]
r5dip = rv_data_d5_dip.iloc[:,0]; p5dip = rv_data_d5_dip.iloc[:,1]
r25dip = rv_data_d25_dip.iloc[:,0]; p25dip = rv_data_d25_dip.iloc[:,1]
# r5 = rv_data_d5.iloc[:,0]; p5 = rv_data_d5.iloc[:,1]
# r05 = rv_data_d05.iloc[:,0]; p05 = rv_data_d05.iloc[:,1]

# p50dif = abs(p50dip - p50)*1000

fig, ax = plt.subplots(figsize = (12, 10))

# ax.plot(r05, p05, 'r-', linewidth = 5, label = 'd = 0.5 nm')
# ax.plot(-r05, p05, 'r-', linewidth = 5)
# ax.plot(r5, p5, 'b-', linewidth = 5, label = 'd = 5.0 nm')
# ax.plot(-r5, p5, 'b-', linewidth = 5)

ax.plot(r50dip, p50dip, 'k', linewidth = 3, label = 'd = 50.0 nm')
ax.plot(-r50dip, p50dip, 'k-', linewidth = 3)
ax.plot(r1dip, p1dip, 'b-', linewidth = 3, label = 'd = 1.0 nm')
ax.plot(-r1dip, p1dip, 'b-', linewidth = 3)
ax.plot(r5dip, p5dip, 'r-', linewidth = 3, label = 'd = 5.0 nm')
ax.plot(-r5dip, p5dip, 'r-', linewidth = 3)
ax.plot(r25dip, p25dip, 'g-', linewidth = 3, label = 'd = 25.0 nm')
ax.plot(-r25dip, p25dip, 'g-', linewidth = 3)

ax.set_xlabel('r (nm)', fontsize = 40, fontweight = 'bold', fontname = "Arial")
ax.set_ylabel('$\mathregular{\Phi}$$^{(0)}$ (V)', fontsize = 40, fontweight = 'bold', fontname = "Arial")

ax.tick_params(axis = 'x', direction = 'in', labelsize = 32, length = 10)
ax.tick_params(axis = 'x', direction = 'in', which = 'minor', length = 6)
ax.tick_params(axis = 'y', direction = 'in', which = 'minor', length = 6)
ax.tick_params(axis = 'y', direction = 'in', labelsize = 32, length = 10)

ax.ticklabel_format(style='sci', axis='x', scilimits=(0,4))

ax_xmajor = np.arange(-500, 500.1, 250)
ax_xminor = np.arange(-500, 500.1, 50)

ax_ymajor = np.arange(0.3, 1.001, .1)
ax_yminor = np.arange(0.3, 1.001, .05)

ax.set_xlim([-500, 500])
ax.set_ylim([0.25, 1.05])

ax.set_xticks(ax_xmajor)
ax.set_xticks(ax_xminor, minor = True)
ax.set_yticks(ax_ymajor)
ax.set_yticks(ax_yminor, minor = True)

for tick in ax.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax.get_yticklabels():
    tick.set_fontname("Arial")
    
# ax.grid(which = 'major', axis = 'both', color = 'gray', linestyle = '--')

L = ax.legend(loc = 'upper right', prop = {"size": 28})
plt.setp(L.texts, family='Arial')

#Set filename and path
my_path = os.path.abspath('/Users/MG/Dropbox/0. Research/2. Tribocharge nanopatterning/Electrostatic Simulation/11152020-')
my_file = 'Dip_flatandnanocup_d1_5_25_50nm_z0.png'
# fig.tight_layout()
fig.savefig(os.path.join(my_path, my_file), dpi = 300)
"""
#%% Difference Plot

fig2, ax2 = plt.subplots(figsize = (12, 10))

ax2.plot(r50, p50dif, 'g-', linewidth = 3, label = 'd = 50.0 nm')
ax2.plot(-r50, p50dif, 'g-', linewidth = 3)

ax2.set_xlabel('r (nm)', fontsize = 40, fontweight = 'bold', fontname = "Arial")
ax2.set_ylabel('$\mathregular{\Phi}$$^{(0)}$ (mV)', fontsize = 40, fontweight = 'bold', fontname = "Arial")

ax2.tick_params(axis = 'x', direction = 'in', labelsize = 32, length = 10)
ax2.tick_params(axis = 'x', direction = 'in', which = 'minor', length = 6)
ax2.tick_params(axis = 'y', direction = 'in', which = 'minor', length = 6)
ax2.tick_params(axis = 'y', direction = 'in', labelsize = 32, length = 10)

ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,4))

ax_xmajor = np.arange(-500, 500.1, 250)
ax_xminor = np.arange(-500, 500.1, 50)

ax_ymajor = np.arange(0, 101, 20)
ax_yminor = np.arange(0, 101, 5)

ax2.set_xlim([-520, 520])
ax2.set_ylim([-10, 110])

ax2.set_xticks(ax_xmajor)
ax2.set_xticks(ax_xminor, minor = True)
ax2.set_yticks(ax_ymajor)
ax2.set_yticks(ax_yminor, minor = True)

for tick in ax2.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Arial")
    
# ax.grid(which = 'major', axis = 'both', color = 'gray', linestyle = '--')

L = ax2.legend(loc = 'upper right', prop = {"size": 28})
plt.setp(L.texts, family='Arial')

#Set filename and path
my_path = os.path.abspath('/Users/MG/Dropbox/0. Research/2. Tribocharge nanopatterning/Electrostatic Simulation/11152020-')
my_file = 'Dip_flatandnanocup_difference_d50nm_z0.png'
# fig.tight_layout()
fig2.savefig(os.path.join(my_path, my_file), dpi = 300)
"""