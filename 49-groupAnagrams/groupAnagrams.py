class Solution:



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            



        # map = defaultdict(list)
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     map[sorted_s].append(s)
        # return list(map.values())
    
        # hashTable = defaultdict(list)
        # for s in strs:
        #     sort_s = ''.join(sorted(s))
        #     if sort_s not in hashTable:
        #         hashTable[sort_s] = list([])
        #     hashTable[sort_s].append(s)
        # return list(hashTable.values())


        # defaultStrList = defaultdict(list)
        # for s in strs:
        #     sorted_s = "".join((sorted(s)))
        #     defaultStrList[sorted_s].append(s)
        
        # return list(defaultStrList.values())

        # res = defaultdict(list)

        # for str in strs:
        #     sorted_s = "".join(sorted(str))
        #     res[sorted_s].append(str)

        # return list(res.values())

        # hash_list = defaultdict(list)

        # for str in strs:
        #     sorted_s = ''.join(sorted(str))

        #     hash_list[sorted_s].append(str)

        # return list(hash_list.values())