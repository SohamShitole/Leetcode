class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
    #Brute force method: Sorting arrays first and then see whether it is equal or not
        x = sorted(s)
        y = sorted(t)
        if x == y:
            return True
        else:
            return False

    sol = Solution()
    result = sol.isAnagram("anagram", "nagaram")
    print(result)  # This will print 'True' if they are anagrams, 'False' otherwise


