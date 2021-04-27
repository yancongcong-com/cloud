a = 1


def func():
    a = 2
    b = 4

    def func2():
        nonlocal a
        a = 100
        nonlocal b
        b = 200
        print("fun2", b)
        print("fun2", a)

    func2()
    print("fun", b)
    print("fun", a)


func()
print("funcwai", a)
