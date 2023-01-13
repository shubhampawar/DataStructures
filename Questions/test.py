def longest_palindromic_substring(s):
    # base case: if the string is empty or has length 1, it is a palindrome
    if len(s) <= 1:
        return s

    # initialize a table to store the solutions to the subproblems
    n = len(s)
    table = [[False] * n for _ in range(n)]

    # all substrings of length 1 are palindromes
    for i in range(n):
        table[i][i] = True

    # store the start and end indices of the longest palindromic substring
    start = 0
    end = 0

    # solve the subproblems
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            # if the characters at the ends of the substring are the same, and the
            # substring between them is a palindrome, then the whole substring is a palindrome
            if s[i] == s[j] and (j - i <= 2 or table[i + 1][j - 1]):
                table[i][j] = True
                if j - i > end - start:
                    start = i
                    end = j

    # return the longest palindromic substring
    return s[start:end + 1]
longest_palindromic_substring("aacabdkacaa")

Worked on Python 3.7
Worked on AWS - (Developer Associate Certification passed)
Knowledge on Gitlab pipeline /Azure Devops
API Development





