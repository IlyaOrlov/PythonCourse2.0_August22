from multiprocessing import Pool


def sum_smth(lst):
    return lst[0] + lst[1]


if __name__ == "__main__":
    lst = ([1, 3],
           ["abc", "def"],
           [[1, 2, 3], [4, 5, 6]])
    pool = Pool(processes=4)
    res = pool.map(sum_smth, lst)
    print(res)

