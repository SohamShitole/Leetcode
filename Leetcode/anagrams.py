class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
    #Brute force method: Sorting arrays first and then see whether it is equal or not
        # x = sorted(s)
        # y = sorted(t)
        # if x == y:
        #     return True
        # else:
        #     return False
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        for i in t:
            if i in hash_map:
                hash_map[i] -= 1
                if hash_map[i] < 0:
                    return False
            else:
                return False
        return True
            

sol = Solution()
result = sol.isAnagram("anagram", "nagram")
print(result)  # This will print 'True' if they are anagrams, 'False' otherwise


