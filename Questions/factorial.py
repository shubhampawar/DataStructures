def fact(num):
    # print(num)
    if num == 1:
        return num
    print(num*fact(num-1))
    return num*fact(num-1)


print(fact(19))
