"""
*
**
***
****
*****
"""

n = 5
for i in range(1,n+1):
    print("*"*i)



"""
1
22
333
4444
55555
"""

count = 1
for i in range(1,n+1):
    print(str(i)*i)


"""
1
23
456
78910
"""

c = 1

for i in range(n):
    for j in range(i):
        print(c,end="")
        c+=1
    print("\n")