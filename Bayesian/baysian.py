import pandas as pd
import math as mp
import numpy as np
import matplotlib.pyplot as plt

def find_match(test ,ind, clss, inp):
	count = 0
	for i in range(len(inp[len(inp)-1])):
		if inp[len(inp)-1][i] == clss and inp[ind][i] == test:
			count = count+1
	return count

def laplacian(inp):
	temp = []
	for i in range(len(inp)):
		if inp[i] not in temp:
			temp.append(inp[i])
	return len(temp)

def find_count(clss , inp):
	count = 0
	for i in inp:
		if clss == i:
			count = count + 1
	return count

def apply_baysian(inp, test, clss):
	maxi = 0
	ans_clss = None
	for i in range(len(clss)):

		ans = find_count(clss[i],inp[len(inp)-1])/len(inp[len(inp)-1])
		for j in range(len(inp)-1):
			if find_match(test[j],j ,clss[i], inp) != 0:
				ans = ans *(find_match(test[j],j ,clss[i], inp)/find_count(clss[i],inp[len(inp)-1]))
				print(find_match(test[j],j ,clss[i], inp)/find_count(clss[i],inp[len(inp)-1]))
			else :
				ans = ans*(1/((find_count(clss[i],inp[len(inp)-1]))+laplacian(inp[j])))
				print(1/((find_count(clss[i],inp[len(inp)-1]))+laplacian(inp[j])))
		print(clss[i]+' The baysian probability is :'+str(ans) )
		if ans > maxi:
			maxi = ans
			ans_clss = clss[i]

	return ans_clss


def load_input(filename):
	df = pd.read_excel(filename)
	x = df.to_records()
	x = [list(elem) for elem in x]
	x = np.array(x)
	x = x.T
	x = np.delete(x,1,0)
	x = np.delete(x,0,0)
	return x
	
def main():
	filename = 'dataset.xlsx'
	inp = load_input(filename)
	test = []
	clss = []
	# for i in range(len(inp)-1):
	# 	test.append(input())
	test.append('T')
	test.append('T')
	test.append('F')
	test.append('T')
	test.append('Some')
	test.append('$$$')
	test.append('T')
	test.append('T')
	test.append('Italian')
	test.append('>60')
	for i in range(len(inp[len(inp)-1])):
		if inp[len(inp)-1][i] not in clss:
			clss.append(inp[len(inp)-1][i])

	ans = apply_baysian(inp,test,clss)
	print('With the highest value the class will be :'+str(ans))
if __name__ == '__main__':
	main()