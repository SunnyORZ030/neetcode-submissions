class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexStack = []
        ansStack = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while indexStack and temperature > temperatures[indexStack[-1]]:
                lastIndex = indexStack.pop()
                ansStack[lastIndex] = i - lastIndex
                    
            indexStack.append(i)

        return ansStack