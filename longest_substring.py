class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:        
            
        max_s = ""        
        
        for i in range(len(s)):
            sub_string =""
            
            for c in s[i:]:
                if c not in sub_string:
                    sub_string +=c
                else:
                    break 
            
            if len(sub_string)> len(max_s):
                max_s = sub_string
        
        return len(max_s)