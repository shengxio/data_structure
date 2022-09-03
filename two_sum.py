class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse = [target - n for n in nums]
        
        for i in range(len(reverse)):
            try:
                reverse_i = nums.index(reverse[i])
                if i!=reverse_i:
                    return [i,reverse_i]
            except:
                pass