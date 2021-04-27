from moduleB import b


def a():
    print("a is a func a")
    moduleB.b()


def c():
    print('a is a func c')


if _name_ == '_main_':
    c()
