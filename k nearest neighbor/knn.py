from csv import reader
from sys import exit
from math import sqrt
from operator import itemgetter
import numpy as np

def load_data_set(filename):
    with open(filename, newline='') as iris:
        return list(reader(iris, delimiter=','))


def convert_to_float(data_set, mode):
    new_set = []
    if mode == 'training':
        for data in data_set:
            new_set.append([float(x) for x in data[:len(data)-1]] + [data[len(data)-1]])

    elif mode == 'test':
        for data in data_set:
            new_set.append([float(x) for x in data])

    else:
        print('Invalid mode, program will exit.')
        exit()

    return new_set

def get_classes(training_set):
    return list(set([c[-1] for c in training_set]))


def find_neighbors(distances, k):
    return distances[0:k]


def find_response(neighbors, classes):
    votes = [0] * len(classes)

    for instance in neighbors:
        for ctr, c in enumerate(classes):
            if instance[-2] == c:
                votes[ctr] += 1

    return max(enumerate(votes), key=itemgetter(1))


def knn(training_set, test_set, k):
    distances = []
    dist = 0
    limit = len(training_set[0]) - 1
    classes = get_classes(training_set)
    for test_instance in test_set:
        for row in training_set:
            for x, y in zip(row[:limit], test_instance):
                dist += (x-y) * (x-y)
            distances.append(row + [sqrt(dist)])
            dist = 0

        distances.sort(key=itemgetter(len(distances[0])-1))
        neighbors = find_neighbors(distances, k)
        index, value = find_response(neighbors, classes)
        print('The predicted class for sample ' + str(test_instance) + ' is : ' + classes[index])

        distances.clear()


def main():

    k = int(input('Enter the value of k : '))
    training_file = 'iris-dataset.csv'
    test_file = 'iris-test.csv'
    training_set = convert_to_float(load_data_set(training_file), 'training')
    test_set = convert_to_float(load_data_set(test_file), 'test')
    np.random.shuffle(test_set)
    knn(training_set, test_set, k)


if __name__ == '__main__':
    main()
