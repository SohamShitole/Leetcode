from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_counter = {}
        for i in nums:
            if i in freq_counter:
                freq_counter[i] += 1
            else:
                freq_counter[i] = 1 
        
        res = nlargest(k, freq_counter, key=freq_counter.get)
        return res

            


sol = Solution()
input_nums = [1,1,2,2,2,3]
input_k = 2
result = sol.topKFrequent(input_nums, input_k)
print(result)