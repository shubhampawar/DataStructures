def get_bin(n):
    ans = ""
    while n:
        rem = n%2
        ans+=str(rem)
        n//=2
        # print(ans)

    return ans[::-1]

n = 14
binary = get_bin(n)

print(binary,bin(n).replace("0b",""))


print(binary == bin(n).replace("0b",""))
