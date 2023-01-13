def reverse(num):
    ans = 0
    while num >0:
        r = num%10
        num = num//10
        ans = ans*10+r

        print(ans)
    return ans

print(reverse(1234))
