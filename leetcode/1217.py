"""
    https://leetcode.cn/problems/minimum-cost-to-move-chips-to-the-same-position/
    1217. 玩筹码
    有 n 个筹码。第 i 个筹码的位置是 position[i] 。
    
    我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 i 个筹码的位置从 position[i] 改变为:
    
    position[i] + 2 或 position[i] - 2 ，此时 cost = 0
    position[i] + 1 或 position[i] - 1 ，此时 cost = 1
    返回将所有筹码移动到同一位置上所需要的 最小代价 。
    
     
    
    示例 1：
    
    
    
    输入：position = [1,2,3]
    输出：1
    解释：第一步:将位置3的筹码移动到位置1，成本为0。
    第二步:将位置2的筹码移动到位置1，成本= 1。
    总成本是1。
    示例 2：


"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        tmp = [0, 0]
        for idx in position:
            if idx & 1 == 0:
                tmp[0] += 1
            else:
                tmp[1] += 1
        return min(tmp)
