class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_num = {}
        for num in nums:
            if num not in seen_num:
                seen_num[num] = 1
            else:
                seen_num[num] += 1
        
        return sorted(seen_num, key=seen_num.get, reverse=True)[:k]