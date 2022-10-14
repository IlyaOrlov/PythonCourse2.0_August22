from multiprocessing import Pool


def sum_smth(inner_list):
    a = inner_list[0]
    match a:
        case list(a):
            res = []
            for i in inner_list:
                res += i
        case str(a):
            res = ""
            for i in inner_list:
                res += i
        case int(a):
            res = 0
            for i in inner_list:
                res += i
    return res


if __name__ == "__main__":
    lst = ([1, 3, 5],
           ["abc", "def"],
           [[1, 2, 3, 10], [4, 5, 6]])
    pool = Pool(processes=4)
    res = pool.map(sum_smth, lst)
    print(res)

