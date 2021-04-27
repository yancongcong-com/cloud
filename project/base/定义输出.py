from functools import reduce

print(reduce(lambda x, y: x * 10 + y, list(map(lambda x: int(x), list('12345')))))

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def func(arr):
#     for x in arr:
#         if x % 2 == 0:
#             arr.remove(x)


# func(li)
def func(num):
    if num % 2 == 0:
        return False
    return True


res = filter(func, li)

print(res)
print(list(res))
print(li)
