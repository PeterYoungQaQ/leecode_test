
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in dic:
                dic[sorted_x].append(x)
            else:
                dic[sorted_x] = [x]
        
        return list(dic.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        