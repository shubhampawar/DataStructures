"""
1 2 3
4 5 6
7 8 9
"""


def pattern(n=6):
    for i in range(1,n+1 ):
        print(i,end=" ")
        if i%3 == 0:
            print("\n")

num = int(input("enter num"))
pattern(num)
