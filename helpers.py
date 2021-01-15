from copy import deepcopy
from random import getrandbits

class BinList:
    # List that contains a binary number, smallest bit left
    # Usefull for generating all subpolyiamonds of a polyiamond
    def __init__(self, length: int, data: list = [0]):
        self.list = data
        self.len = length

    def __iter__(self):
        return self

    def __next__(self):
        self.list = deepcopy(self.list)
        max = len(self.list)
        if max < self.len:
            for i in range(0,max):
                if not self.list[i]:
                    self.list[i] = True - self.list[i]
                    break
                self.list[i] = True - self.list[i]
                try:
                    self.list[i+1]
                except IndexError:
                    self.list.append(1)
            return self.list
        raise StopIteration

class RandomBinList:
    # Generates a random bin list of the given length
    def __init__(self, length: int, count: int):
        self.len = length
        self.randomlist = []
        self.max_count = count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.max_count:
            self.randomlist = []
            self.count += 1
            for i in range(0,self.len):
                self.randomlist.append(getrandbits(1))
            return self.randomlist
        raise StopIteration

class SubsetList:
    # List that contains all subsets of a certain size
    def __init__(self, set_size: int, subset_size: int):
        self.list = []
        for i in range(subset_size):
            self.list.append(1)
        for i in range(subset_size, set_size):
            self.list.append(0)

    def __iter__(self):
        return self

    def __next__(self):
        self.list = next(self.list)
        return self.list

def next(list):
    if len(list) <= 1:
        raise StopIteration
    for i in range(len(list)-1, -1, -1):
        if list[i] == 1:
            if i == len(list)-1:
                # recursion!
                list = next(list[:-1])
                list.append(0)
                for j in range(len(list)-1, -1, -1):
                    if list[j] == 1:
                        list[j+1] = 1
                        return list
            else:
                # the swaping
                a = list[i]
                b = list[i+1]
                list[i] = b
                list[i+1] = a
                return list
    raise StopIteration
