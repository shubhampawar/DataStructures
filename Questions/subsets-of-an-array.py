def foo(l):
    if len(l) == 0:
        return [[]]

    return foo(l[:-1]) + [[l[-1]] + y for y in foo(l[:-1])]


print(foo(["a", "b", "c"]))
