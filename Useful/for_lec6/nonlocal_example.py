def fun():
    def inner_fun():
        def inner_fun2():
            nonlocal x
            print(f"Local x: {x}")

        inner_fun2()

    x = 500
    inner_fun()
    print(f"Local x: {x}")


x = 1000
fun()
print(f"Global x: {x}")
