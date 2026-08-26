class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana = {}
        anb = {}

        for i in s:
            if i not in ana:
                ana[i] = 1
            else:
                ana[i] += 1

        for i in t:
            if i not in anb:
                anb[i] = 1
            else:
                anb[i] += 1
        return ana == anb
        