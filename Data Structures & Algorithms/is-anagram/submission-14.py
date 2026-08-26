class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ana = {}
        anb = {}

        for i in s:
            ana[i] = ana.get(i,0)+1 #skip for loop, better for single hash lookup
        for i in t:
            anb[i] = anb.get(i,0)+1
        return ana == anb 
