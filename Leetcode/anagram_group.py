class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs_dict = {}
        dict1 = {}
        for i in strs:
            sorted_i = ''.join(sorted(i))
            strs_dict[i] = sorted_i
            if sorted_i not in dict1:
                dict1[sorted_i] = [i]
            else:
                dict1[sorted_i].append(i)


            
        
        return list(dict1.values())








sol = Solution()
input_list = ["",""]
result = sol.groupAnagrams(input_list)
print(result)
