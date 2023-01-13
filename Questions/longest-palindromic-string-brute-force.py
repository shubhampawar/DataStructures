class Solution:
    ans = 0
    def isPalindrome(self,a):
        return a == a[::-1]

    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        for i in range(l+1):
            for j in range(i,l+1):
                self.isPalindrome(s[i:j])
                ans = max(ans,len(s[i:j]))

        return ans


s = Solution()
s.longestPalindrome("babad")
