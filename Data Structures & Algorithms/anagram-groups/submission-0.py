class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new=[]
        for n in strs :
            n=sorted(n)
            new.append(''.join(n))

        dict={}

        for letters , word in zip(new, strs):
            letters ,word

            if (letters not in dict):
                dict[letters]=[word]
            else:
                dict[letters].append(word)
    
        strs=list(dict.values())
        return strs 
