class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = {}
        anb = {}

        for i in s:
            ana[i] = ana.get(i,0)+1
        for i in t:
            anb[i] = anb.get(i,0)+1
        return ana == anb 
