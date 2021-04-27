def wrapper(f):
    def inner(*args, **kwargs):
        print("***************")
        res = f(*args, **kwargs)
        return res

    return inner()


def a(name, age):
    return "%s is a good man ,is %d yes" % (name, age)


an = wrapper(a)
print(a("sadd", 12))
