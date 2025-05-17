import numpy
import pandas

loop = int(10)
distancetemp = 0
distance = 0
number = 0
file = 'input.txt'
inputs = pandas.read_csv(file, header=None, sep='\s+', names=['col1', 'col2'])
col1 = inputs['col1'].values
col2 = inputs['col2'].values

col1.sort()
col2.sort()


for x in col1:
    number = len(numpy.argwhere(col2==x))
    distance = distance+(x * number)
    
print("Total distance: "+str(distance))


