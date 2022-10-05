def myrange(*args):
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) > 1:
        start = args[0]
        stop = args[1]
        if len(args) == 3:
            step = args[2]
    else:
        raise TypeError("range expected at least 1 argument, got 0")

    if step == 0:
        raise TypeError("step should not be 0")

    fun = lambda: start < stop if step > 0 else start > stop

    while fun():
       yield start
       start += step


for i in myrange(10, 1, -1):
    print(i)