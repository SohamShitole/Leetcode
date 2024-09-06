class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         a = nums[i] + nums[j]
        #         if a == target:
        #             b = [i,j]
        #             return b

        num_dict = {}
        for index,num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[num] = index