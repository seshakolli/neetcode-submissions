class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_clean="".join(char.lower() for char in s if char.isalnum())
        n=len(str_clean)
        j=n-1
        for i in range(0, n//2):
            if str_clean[i]==str_clean[j]:
                j-=1
            else:
                return False
        return True


