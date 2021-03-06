import matplotlib.pyplot as plt
import numpy as np
import sys

glass_raw = "raw-data/Sp15_245L_sect-001_group-1_glass.raw"
ultem_raw = "raw-data/Sp15_245L_sect-001_group-1_ultem.raw"
steel_raw = "raw-data/Sp15_245L_sect-001_group-2-4_bendtest-steel.raw"
aluminum_spec_1 = "raw-data/aluminum.raw"
aluminum_spec_2 = "raw-data/aluminum_2.raw"
aluminum_spec_3 = "raw-data/aluminum_3.raw"
tungsten_spec_1 = "raw-data/tungsten.raw"
tungsten_spec_2 = "raw-data/tungsten_2.raw"
tungsten_spec_3 = "raw-data/tungsten_3.raw"

filename = sys.argv[1] 
data = np.loadtxt(filename,skiprows=32,delimiter=',')
x = data[3]*-1
y = data[7]*-1

slope = np.polyfit(x,y,1) 
poly1d_youngs = np.poly1d(slope)
plt.plot(x,poly1d_youngs(x),'--k',label = 'fit')
plt.plot(x,y,'b',label = 'data')

plt.title(filename)
plt.grid(True)
plt.xlabel("Strain [Ext %]")
plt.ylabel("Stress [MPa]")
plt.legend(loc='best')

plt.text(5000, 100000 , "Young's Modulus = {:.3f} MPa".format(slope[0]))

plt.savefig(filename+".png")
plt.show()


## Part 0
# Figure out what arguments to add to the loadtxt function call
# so that numbers are loaded into the local function 'data'.
# Hint: look for arguments like 'skiprows' and 'delimiter'
# Check by running:
#   $ pythonap.py raw-data/Sp15_245L_sect-001_group-1_glass.raw
# at the command line.


## Part 1
# Figure out what columns and rows of data we need to plot
# Stress (y-axis) vs Strain (x-axis)
# plot raw-data/Sp15_245L_sect-001_group-1_glass.raw
# Make sure to include axis labels and units!
# plt.plot(xdata,ydata, arguments-to-make-plot-pretty)


## Part 2
# Check to see if your code in part 1 will plot all of the files in raw-data/
# Edit the files (use git liberally here!) to make them more usable


## Part 3
# Use linear regression to calculate the slope of the linear part of
# the stress-strain data. Plot your line against the data to make 
# sure it makes sense! Use the slope of this line to calculate and print
# the Young's modulus (with units!)


## Part 4
# Modify your code to save your plots to a file and see if you can generate
# plots and Young's moduli for all of the cleaned up files in your data 
# directory. If you haven't already, this is a good time to add text to 
# your .gitignore file so you're not committing the figures to your repository.



