class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        start = -1
        count = 0
        hmap1 = {}
        hmap2 = {}
        minlen = len(s)

        for i in t:
            hmap1[i] = hmap1.get(i, 0) + 1

        while r < len(s) or count == len(hmap1):

            while count == len(hmap1):
                if r - l  <= minlen:
                    minlen = r - l 
                    start = l

                if s[l] in hmap1 and hmap1[s[l]] == hmap2[s[l]]:
                    count -= 1

                hmap2[s[l]] -= 1

                if hmap2[s[l]] == 0:
                    del hmap2[s[l]]

                l += 1

            if count != len(hmap1) and r < len(s):
                hmap2[s[r]] = hmap2.get(s[r], 0) + 1

                if s[r] in hmap1:
                    if hmap1[s[r]] == hmap2[s[r]]:
                        count += 1

                r += 1

        if start == -1:
            return ""

        return s[start:start + minlen]