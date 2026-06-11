# https://leetcode.com/problems/daily-temperatures/description/
from typing import List
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans=[0]*len(temperatures)
    stack=[]
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            last_idx = stack.pop()
            ans[last_idx]=i-last_idx
        stack.append(i)
    return ans

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))