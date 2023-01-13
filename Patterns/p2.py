"""
matrix of goiven number
5*5


12345
678910
"""

def pattern(n=5):
    count = 1
    for i in range(5):
        for _ in range(n):
            print(count,end=" ")
            count+=1
        print("\n")

pattern()
