# https://leetcode.com/problems/baseball-game/description/
from typing import List
def calPoints(operations: List[str]) -> int:
    ans=[]
    for ch in operations:
        try:
            num=int(ch)
            ans.append(num)
        except ValueError:
            if ch == "+":
                ans.append(ans[-1] + ans[-2])
            if ch == "D":
                ans.append(ans[-1]*2)
            if ch == "C":
                ans.pop()
    return sum(ans)

ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))