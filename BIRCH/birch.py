from sklearn.cluster import Birch
import matplotlib as mpl
import matplotlib.pyplot as plt

def convert_to_int(inp):
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

def plot_points(label, x):
	colors = ['r', 'b' , 'g', 'pink' , 'aqua' ,'orange' , 'k' , 'purple']
	plt.axis('off')
	for i in range(len(x)):
		plt.plot(x[i][0], x[i][1], marker='.', markerfacecolor=colors[label[i]],markeredgecolor='k')
	plt.title('Birch clustering')
	plt.show()

def main():
	filename = 'dataset.txt'
	x = convert_to_int(load_input(filename))
	brc = Birch(branching_factor=50, n_clusters=7, threshold=0.5,compute_labels=True)
	ans = brc.fit_predict(x)
	plot_points(ans,x)

if __name__ == '__main__':
	main()