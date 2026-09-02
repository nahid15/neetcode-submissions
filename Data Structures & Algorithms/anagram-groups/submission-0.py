class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gana = {}
        for st in strs:
            c = [0] * 26
            for i in st:
                idx = ord(i) - ord("a")
                c[idx] += 1
            key = tuple(c)
            if key not in gana:
                gana[key] = [st]
            else:
                gana[key].append(st)
        return list(gana.values())

    