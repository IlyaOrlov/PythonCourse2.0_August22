# -*- coding: utf-8 -*-
from multiprocessing import Pool

def addition(data):
    t = data[0]
    match t:
        case int(t):
            res = 0
            for y in data:
                res += y
        case str(t):
            res = ""
            for y in data:
                res += y
        case list(t):
            res = []
            for y in data:
                res += y
    return res



if __name__ == '__main__':
    data = ([1, 2, 4], [[1, 2], [4, 7], [9, 0]], ["Hello", "world"])
    pool = Pool(processes=3)
    res = pool.map(addition, data)
    print(res)

