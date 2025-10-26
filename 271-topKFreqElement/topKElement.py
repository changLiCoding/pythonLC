class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums)
        # bucket = [[] for _ in range(n + 1)]
        # counter = Counter(nums)
        # for n, freq in counter.items():
        #     bucket[freq].append(n)
        # res = []
        # for i in range(n, -1, -1):
        #     nList = bucket[i]
        #     if len(nList) > 0:
        #         for n in nList:
        #             res.append(n)
        #             if len(res) == k:
        #                 return res
        # return res

        # n = len(nums)
        # bucket = [[] for _ in range(n + 1)]
        # counter = Counter(nums)
        # for i, (key, counter) in enumerate(counter.items()):
        #     bucket[counter].append(key)
        # res = []
        # for i in range(n, -1, -1):
        #     if len(bucket[i]) > 0:
        #         for n in bucket[i]:
        #             if len(res) < k:
        #                 res.append(n)
        #             else:
        #                 return res
        # return res
                    
            
        # counter = Counter(nums)
        # def_dict = defaultdict(list)
        # res = counter.most_common(k)
        # return [item[0] for item in res]

        # res = []
        # n = len(nums)
        # count = Counter(nums)
        # bucket = [[] for _ in range(n + 1)]
        # for num, frq in count.items():
        #     bucket[frq].append(num)
        # for i in range(n, -1, -1):
        #     if len(bucket[i]) > 0:
        #         for num in bucket[i]:
        #             res.append(num)
        #             if len(res) == k:
        #                 return res
        # return res
