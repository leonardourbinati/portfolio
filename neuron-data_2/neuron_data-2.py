# neuron-data_2 list

f=open('neuron_data-2.txt','r')
L1=[]; L2=[]
for line in f:
	column= line.split()
	if column[0]=='1':
		L1.append(column[0:])
	else:
		L2.append(column[0:])
for e in L1:
	print('%s' %e)
for e in L2:
	print('%s' %e)

# neuron-data_2 average

L1=[]
L2=[]
def average(L1,L2):
	f=open('neuron_data-2.txt','r')
	for line in f:
		column= line.split()
		if column[0]=='1':
			L1.append(float(column[1]))
		else:
			L2.append(float(column[1]))

	L1_average = sum(L1)/float(len(L1))
	L2_average = sum(L2)/float(len(L2))
	return('\nprimary neuron average= %s \nsecondary neuron average= %s' %(L1_average, L2_average))
print average(L1,L2)

# neuron-data_2 standard deviation

L1=[]
L2=[]
def st_dev(L1,L2):
	from math import sqrt
	f=open('neuron_data-2.txt','r')
	for line in f:
		column= line.split()
		if column[0]=='1':
			L1.append(float(column[1]))
		else:
			L2.append(float(column[1]))

	L1_average = sum(L1)/float(len(L1))
	L2_average = sum(L2)/float(len(L2))
	
	quadratic_deviation=0.0
	for number in L1:
		quadratic_deviation+= (number-L1_average)**2
	st_dev_1= sqrt(quadratic_deviation/len(L1))
	for number in L2:
		quadratic_deviation+= (number-L2_average)**2
	st_dev_2= sqrt(quadratic_deviation/len(L2))
	return('\nst dev 1= %s \nst dev 2= %s' %(st_dev_1, st_dev_2))
print st_dev(L1,L2)

# neuron-data_2_bis.txt file

g= open('neuron-data_2_bis.txt','w')

data_1=[1,2,2,1,1,2,1,2,2]
data_2=[16.38,139.90,441.46,29.03,40.93,202.07,142.30,346.00,300.00]
for e in range(len(data_1)):	
	g.write(str(data_1[e]) + '\t' + str(data_2[e]) + '\n')
g.write('\n')
g.close()

# neuron-data_2_bis.txt.file again

g= open('neuron-data_2_bis.txt','a')

data_1=[1,2,2,1,1,2,1,2,2]
data_2=[16.38,139.90,441.46,29.03,40.93,202.07,142.30,346.00,300.00]
for e in range(len(data_1)):	
	g.write('%i%s%f%s' %(data_1[e], '\t', data_2[e], '\n'))
g.close()

# number of primary and secondary neurons, total length, the shortest and the longest.

data_1= []

for line in open('neuron_data-2.txt'):
    columns = line.split()
    if columns[0]=='1':
        data_1.append(float(columns[1]))

n_primary_neurons= len(data_1)
total_lenght= sum(data_1)
shortest = min(data_1)
longest = max(data_1)

h= open("neuron_data_summary.txt","w")
h.write("number of primary neurons data: %2i \n"%(n_primary_neurons))
h.write("tot length: %4.1f \n"%(total_lenght))
h.write("shortest length: %4.2f \n"%(shortest))
h.write("longest length: %4.2f \n"%(longest))
h.close()

data_2=[]

for line in open('neuron_data-2.txt'):
    columns = line.split()
    if columns[0]=='2':
        data_2.append(float(columns[1]))

n_secondary_neurons= len(data_2)
total_lenght= sum(data_2)
shortest = min(data_2)
longest = max(data_2)

h= open("neuron_data_summary.txt","a")
h.write('\n')
h.write("number of secondary neurons data: %2i \n"%(n_secondary_neurons))
h.write("tot length: %4.1f \n"%(total_lenght))
h.write("shortest length: %4.2f \n"%(shortest))
h.write("longest length: %4.2f \n"%(longest))
h.close()
