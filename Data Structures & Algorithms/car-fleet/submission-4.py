class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        
        ansTime = []
        point = 0

        for po, sp in cars:
            time = (target - po) / sp
            if time > point:
                ansTime.append(time)
                point = time
        
        return len(ansTime)

#[(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
#[1, 1, 7, 3, 12]