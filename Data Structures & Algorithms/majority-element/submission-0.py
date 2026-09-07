class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate=num
                count=1
            elif num==candidate:
                count+=1  
               
            else:
                count-=1

        actual_count=0
        for i in nums:
            if candidate==i:
                actual_count+=1

        if actual_count>len(nums)/2:
            return candidate
        else:
            return -1   