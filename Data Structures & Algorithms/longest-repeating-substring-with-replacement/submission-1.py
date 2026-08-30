class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashmap = {}
        freq = 0
        maxlen = 0

        while r < len(s):

            hashmap[s[r]] = hashmap.get(s[r], 0) + 1

            freq = max(hashmap.values())

            replacement = (r - l + 1) - freq

            while replacement > k:
                hashmap[s[l]] -= 1

                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]

                l += 1

                freq = max(hashmap.values())
                replacement = (r - l + 1) - freq

            maxlen = max(maxlen, r - l + 1)

            r += 1

        return maxlen