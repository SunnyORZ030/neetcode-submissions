class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)
                start = index

            stack.append((start, h))

        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)

        return maxArea