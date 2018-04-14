#!/usr/bin/env python3
"""
ID3 Algorithm for Decision Tree
"""

import csv
from collections import Counter
from anytree import RenderTree, Node
import math
import copy


def read_file(file):
    data = []
    with open(file) as f:
        reader = csv.DictReader(f)
        for line in reader:
            data.append(line)
        fieldnames = reader.fieldnames

    return fieldnames, data


def get_unique(data):
    unique = [set() for _ in data[0]]
    for row in data:
        for index, val in enumerate(row):
            unique[index].add(val)

    return unique


def all_same_class(data, class_attr):
    for row in data[1:]:
        if row[class_attr] != data[0][class_attr]:
            return False

    return True


def find_most_freq(class_data):
    return Counter(class_data).most_common(1)[0][0]


def find_class_info(class_attr, data):
    class_data = [row[class_attr] for row in data]
    classes = set(class_data)
    class_prob = {}
    for cls in classes:
        class_prob[cls] = class_data.count(cls)/len(class_data)

    return -sum([val*math.log(val) for val in class_prob.values()])


def partition(data, attr):
    part_data = {}
    for row in data:
        if row[attr] not in part_data.keys():
            part_data[row[attr]] = []
        part_data[row[attr]].append(row)

    return part_data


def find_non_class_info(non_class_attr, class_attr, data):
    info_non_class = {}
    for attr in non_class_attr:
        part_data = partition(data, attr)
        info = 0
        for key, partial in part_data.items():
            info += len(partial)/len(data) * find_class_info(class_attr, partial)
        info_non_class[attr] = info

    return info_non_class


def find_max_gain(non_class_attr, class_attr, data):
    info_class = find_class_info(class_attr, data)
    info_non_class = find_non_class_info(non_class_attr, class_attr, data)
    print(info_class, info_non_class)

    return max([(key, info_class-val) for key, val in info_non_class.items()])[0]


def build_id3(non_class_attr, class_attr, data, prnt):
    if not data:
        raise Exception("Data empty")

    if all_same_class(data, class_attr):
        Node(data[0][class_attr], parent=prnt)
        return

    if not non_class_attr:
        maxfreqclass = find_most_freq([row[class_attr] for row in data])
        Node(maxfreqclass, parent=prnt)
        return

    max_gain_attr = find_max_gain(non_class_attr, class_attr, data)
    part_data = partition(data, max_gain_attr)
    non_class_attr.remove(max_gain_attr)

    for val in part_data.keys():
        attr = Node(val, parent=prnt, column=max_gain_attr)
        build_id3(copy.deepcopy(non_class_attr), class_attr, copy.deepcopy(part_data[val]), attr)

    return


def main():
    fieldnames, data = read_file('car_data.txt')
    # unique_val = get_unique(data)
    non_class_attr, class_attr = fieldnames[:-1], fieldnames[-1]
    root = Node('root')
    build_id3(non_class_attr, class_attr, data, root)
    print(RenderTree(root))


if __name__ == '__main__':
    main()
