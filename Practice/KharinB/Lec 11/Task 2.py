import multiprocessing as mp
# с точки зрения полезности - программа не очень, но я подумал что раз в условиях задачи идёт речь именно о параллельном
# вычислении, то речь о процессах, а не о потоках.


def my_sum(s):
    if s:
        res = ([] if type(s[0]) == mp.connection.PipeConnection else s.pop(0))
        for g in s:
            if type(g) == mp.connection.PipeConnection:
                break
            res += g
        s[-1].send(res)


def sum_kon_append(*args):
    arg = split_args(args)
    p_res, c_res = mp.Pipe()
    process = []
    for j in arg:
        j.append(c_res)
        proc = mp.Process(target=my_sum, args=(j, ))
        proc.start()
        process.append(proc)

    for proc in process:
        print(p_res.recv())
        proc.join()


def split_args(args):
    str_lst = []
    int_lst = []
    lst_lst = []
    for i in args:
        if type(i) is int:
            int_lst.append(i)
        elif type(i) is str:
            str_lst.append(i)
        elif type(i) is list:
            lst_lst.append(i)
    return (int_lst, str_lst, lst_lst)


if __name__ == "__main__":
    sum_kon_append(73, "73", [73], 1, "1", [1], 5, 9, "Asfd")
