from csv import reader
from sys import exit
from math import sqrt
from operator import itemgetter
import numpy as np

def load_data_set(filename):
	with open(filename, newline='') as iris:
	   return list(reader(iris, delimiter=','))

def converttofloat(data_set, classes):
    new_set = []
    if classes == 0:
        for data in data_set:
            new_set.append([float(x) for x in data[:len(data)-1]] + [data[len(data)-1]])

    if classes == 1:
        for data in data_set:
            new_set.append([float(x) for x in data])

    return new_set

def findcentroid(data_set):
	m = len(data_set[0])-1
	cen1 = []
	cen2 = []
	cen3 = []
	count1 = 0
	count2 = 0
	count3 = 0
	for i in range(m):
		cen1.append(0)
		cen2.append(0)
		cen3.append(0)
	for i in range(len(data_set)):
		if(data_set[i][4]=='Iris-setosa'):
			for j in range(len(data_set[i])-1):
				cen1[j] += data_set[i][j]  
			count1+=1
		if(data_set[i][4]=='Iris-versicolor'):
			for j in range(len(data_set[i])-1):
				cen2[j] += data_set[i][j] 
			count2+=1
		if(data_set[i][4]=='Iris-virginica'):
			for j in range(len(data_set[i])-1):
				cen3[j] += data_set[i][j] 
			count3+=1
	for i in range(len(cen1)):
		cen1[i] = cen1[i]/count1
		cen2[i] = cen2[i]/count2
		cen3[i] = cen3[i]/count3
	return cen1, cen2, cen3

def finddistance(t,c1,c2,c3):
	d1 = np.sqrt((c1[0]-t[0])*(c1[0]-t[0])+(c1[1]-t[1])*(c1[1]-t[1])+(c1[2]-t[2])*(c1[2]-t[2])+(c1[3]-t[3])*(c1[3]-t[3]))
	d2 = np.sqrt((c2[0]-t[0])*(c2[0]-t[0])+(c2[1]-t[1])*(c2[1]-t[1])+(c2[2]-t[2])*(c2[2]-t[2])+(c2[3]-t[3])*(c2[3]-t[3]))
	d3 = np.sqrt((c3[0]-t[0])*(c3[0]-t[0])+(c3[1]-t[1])*(c3[1]-t[1])+(c3[2]-t[2])*(c3[2]-t[2])+(c3[3]-t[3])*(c3[3]-t[3]))
	if( d1<d2 and d1<d3 ):
		return 'Iris-setosa'
	if( d2<d1 and d2<d3 ):
		return 'Iris-versicolor'
	return 'Iris-virginica'

def main():
	training_file = 'iris-dataset.csv'
	test_file = 'iris-test.csv'
	training_set =converttofloat(load_data_set(training_file),0)
	test_set = converttofloat(load_data_set(test_file),1)
	cen1, cen2, cen3 = findcentroid(training_set)
	np.random.shuffle(test_set)
	for i in range(len(test_set)):
		print(training_set[i],'predicted',finddistance(test_set[i],cen1,cen2,cen3))

if __name__ =='__main__':
	main()
