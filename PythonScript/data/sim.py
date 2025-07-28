'''Sample script to demonstrate use of GSASIIscriptable to simulate a powder pattern

This script is described in this tutorial: 
https://advancedphotonsource.github.io/GSAS-II-tutorials/PythonScript/Scripting.htm
'''

import os,sys
sys.path.insert(0,'/Users/toby/software/G2/GSASII')
import GSASIIscriptable as G2sc

workdir = "/Users/toby/Scratch/PythonScript"
datadir = "/Users/toby/software/G2/Tutorials/PythonScript/data"

gpx = G2sc.G2Project(filename='PbSO4sim.gpx') # create a project

# step 1, setup: add a phase to the project
phase0 = gpx.add_phase(os.path.join(datadir,"PbSO4-Wyckoff.cif"),
                      phasename="PbSO4",fmthint='CIF')

# step 2, setup: add a simulated histogram and link it to the previous phase(s)
hist1 = gpx.add_simulated_powder_histogram("PbSO4 simulation",
                          os.path.join(datadir,"inst_d1a.prm"),
                          5.,120.,0.01,
                          phases=gpx.phases())

# Step 3: Set the scale factor to adjust the y scale
hist1.SampleParameters['Scale'][0] = 1000000.

# step 4, compute: turn off parameter optimization and calculate pattern
gpx.data['Controls']['data']['max cyc'] = 0 # refinement not needed
gpx.do_refinements([{}])
gpx.save()

# step 5, retrieve results & plot
x = gpx.histogram(0).getdata('x')
y = gpx.histogram(0).getdata('ycalc')
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.savefig('PbSO4.png') # to show on screen use: plt.show()



