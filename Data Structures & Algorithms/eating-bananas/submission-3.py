import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMin = 1
        kMax = max(piles)
        ans = kMax

        while kMin <= kMax:
            kMid = (kMin + kMax) // 2
            time = 0

            for num in piles:
                time = time + math.ceil(num / kMid)

            if time > h:
                kMin = kMid + 1
            else:
                if ans > kMid:
                    ans = kMid
                kMax = kMid - 1
            
        return ans