def longestPalindrome(self, s: str) -> str:
    longest = s[0]
    for i in range(len(s)):
        for j in range(len(s)-i):
            sub = s[i:i+j+1]
            if len(sub)<=len(longest):
                continue
            if sub == sub[::-1]:
                longest = sub
                
    return longest

def longestPalindrome(self, s: str) -> str:
    longest = s[0]
    for i in range(len(s)):
        for j in range(len(s)-i):
            sub = s[i:i+j+1]
            if len(sub)<=len(longest):
                continue
            if sub == sub[::-1]:
                longest = sub
                
    return longest
