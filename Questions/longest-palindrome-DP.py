def longest_palindromic_substring(s):

    l = len(s)
    table = [[False]* l for _ in range(l)]

    for i in range(l):
        table[i][i] = True

    end,start = 0,0

    for i in range(l-1,-1,-1):
        for j in range(i+1,l):
            if s[i] == s[j] and (i-j <=2 or table[i-1][j+1]):
                table[i][j] = True
                # print(s[i:j+1])
                if j-i > end-start:
                    start = i
                    end = j
    return s[start:end+1]


print(longest_palindromic_substring("abacc"))
