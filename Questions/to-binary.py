def bins(num):
    while num >0:
        r = num%2
        num = num//2
        print(r)

bins(num = 123)
print(bin(123))