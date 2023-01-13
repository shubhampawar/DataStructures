def fibbonaci(num):
    if num <= 1:
        return num
    return fibbonaci(num - 1) + fibbonaci(num - 2)


print(fibbonaci(10))

"""
Fn = {[(√5 + 1)/2] ^ n} / √5 
"""
