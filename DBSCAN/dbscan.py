import math as mp
import numpy 
import matplotlib.pyplot as plt
import matplotlib as mpl

def find_distance(x,y):
    temp = mp.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    return temp

def dbscan(d, eps, minpts): 
    labels = [0]*len(d)  
    c = 0
    for p in range(len(d)):
        if not labels[p]==0 :
            continue

        neighborpts = regionquery(d, p, eps)
        if len(neighborpts) < minpts:
            labels[p] = -1

        else: 
            c += 1
            labels[p] = c
            growcluster(d, labels, p, c, eps, minpts)
    return labels


def growcluster(d, labels, p, c, eps, minpts):
    SearchQueue = [p]
    i = 0
    while i < len(SearchQueue):          
        p = SearchQueue[i]
        neighborpts = regionquery(d, p, eps)
        if len(neighborpts) < minpts:
            i += 1
            continue

        for pn in neighborpts:
            if labels[pn] == -1:
                labels[pn] = c

            elif labels[pn] == 0:
                labels[pn] = c
                SearchQueue.append(pn)
        i += 1        
    


def regionquery(d, p, eps):
    neighbors = []
    for pn in range(0, len(d)):
        if find_distance(d[p] ,d[pn]) < eps:
            neighbors.append(pn)       
    return neighbors



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

def plot_points(inp ,ans):
    plt.axis('off')
    colmap = mpl.cm.ScalarMappable(norm=None, cmap='prism')
    col = colmap.to_rgba(ans)
    for i in range(len(inp)):
            if ans[i] == -1:
                plt.plot(inp[i][0],inp[i][1], marker='.', markerfacecolor='black',markeredgecolor='k')
            else:
                plt.plot(inp[i][0],inp[i][1], marker='.', markerfacecolor=col[i],markeredgecolor='k')
    plt.title('dBScAN')
    plt.show()

def main():
    filename = 'dataset.txt'
    inp = convert_to_float(load_input(filename))
    # eps = float(input('Give the value of eps'))
    # minpts = int(input('Minimum number of points required'))
    eps = 5.1
    minpts = 4
    ans = dbscan(inp,eps, minpts)
    plot_points(inp,ans)

if __name__ == '__main__':
    main()