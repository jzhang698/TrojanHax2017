# A simple script for graphing data.
# Asks for a CSV file containing 2-column data,
# graphs the data then exports to a PDF (vector) file.

import matplotlib.pyplot as plt
import csv
import sys

# allow graphs to be displayed in the console
%matplotlib inline

# import csv file
csv_reader = csv.reader(open('test.csv'))
bigx = float(-sys.maxint -1) 
bigy = float(-sys.maxint -1)
smallx = float(sys.maxint)
smally = float(sys.maxint)

verts = []

for row in csv_reader:
    verts.append(row)
    if float(row[0]) > bigx:
        bigx = float(row[0])
        if float(row[1]) > bigy:
            bigy = float(row[1])
            if float(row[0]) < smallx:
                smallx = float(row[0])
                if float(row[1]) < smally:
                    smally = float(row[1])

# place data in 2 arrays for x and y data
verts.sort()
x_arr = []
y_arr = []

for vert in verts:
    x_arr.append(vert[0])
    y_arr.append(vert[1])

# Create plot
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) #axis size

# write labels
ax.set_xlabel('x data')
ax.set_ylabel('y data')
ax.set_xlim(smallx, bigx)
ax.set_ylim(smally, bigy) #plot range

ax.plot(x_arr, y_arr, color='yellow', lw = 2)
plt.show() # show the plot in the console
fig.savefig('test.pdf') # save plot to file.