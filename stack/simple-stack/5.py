# https://leetcode.com/problems/build-an-array-with-stack-operations/description/
from typing import List
def buildArray(target: List[int], n: int) -> List[str]:
    ans=[]
    target_idx=0
    for i in range(1, n+1):
        if target_idx+1>len(target):
            break
        if i == target[target_idx]:
            ans.append("Push")
            target_idx+=1
        else:
            ans.extend(['Push', 'Pop'])
    return ans


target = [1,2]
n = 4
print(buildArray(target, n))