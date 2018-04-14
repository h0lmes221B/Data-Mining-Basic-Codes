import math as mp
import numpy as np
import matplotlib.pyplot as plt


def find_distance(x,y):
	temp = mp.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
	return temp

def update_mean(mean, cl, k):
	for i in range(k):
		temp1 = 0
		temp2 = 0
		for j in range(len(cl[i])):
			temp1 = temp1 + cl[i][j][0]
			temp2 = temp2 + cl[i][j][1]
		mean[i][0] = temp1/len(cl[i])
		mean[i][1] = temp2/len(cl[i])
	return mean

def plot_points(cl ,k):
	colors = ['r', 'b' , 'g', 'pink' , 'aqua' ,'orange' , 'k' , 'purple']
	plt.axis('off')
	for i in range(k):
		for j in range(len(cl[i])):
			plt.plot(cl[i][j][0], cl[i][j][1], marker='.', markerfacecolor=colors[i],markeredgecolor='k')
	plt.title('K-means clustering')
	plt.show()

def plot_cluster(inp, k):
	cl = []
	mean = []
	for i in range(k):
		cl.append([])
		mean.append(inp[i])
	update_dist = -1
	last_dist = 0
	while last_dist != update_dist :
		cl = []
		for i in range(k):
			cl.append([])
		last_dist = update_dist 
		update_dist = 0
		for x in inp:
			ind = -1
			min_dist = float('inf')
			temp = cl
			for i in range(k):
				if find_distance(mean[i],x) < min_dist :
					min_dist = find_distance(mean[i],x)
					ind = i
			update_dist = update_dist + min_dist
			cl[ind].append(x)
		mean = update_mean(mean,cl,k)
	plot_points(cl, k)

def convert_to_float(inp):
	for i in range(len(inp)):
		for j in range(len(inp[i])):
			inp[i][j] = float(inp[i][j])
	return inp

def load_input(filename):
	file = open(filename,"r")
	temp = []
	for field in file:
		subfield = field.split(" ")
		temp.append(subfield)
	return temp

def main():
	k = int(input('Enter the value of K :'))
	filename = 'dataset.txt'
	inp = convert_to_float(load_input(filename))
	plot_cluster(inp,k)

if __name__ == '__main__':
	main()