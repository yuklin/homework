"""
    https://leetcode.cn/problems/minimum-absolute-difference/
    1200. 最小绝对差
    给你个整数数组 arr，其中每个元素都 不相同。
    
    请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
    
    每对元素对 [a,b] 如下：
    
    a , b 均为数组 arr 中的元素
    a < b
    b - a 等于 arr 中任意两个元素的最小绝对差
    
    
    示例 1：
    
    输入：arr = [4,2,1,3]
    输出：[[1,2],[2,3],[3,4]]
    示例 2：
    
    输入：arr = [1,3,6,10,15]
    输出：[[1,3]]
    示例 3：
    
    输入：arr = [3,8,-10,23,19,-4,-14,27]
    输出：[[-14,-10],[19,23],[23,27]]
    
    
    提示：
    
    2 <= arr.length <= 10^5
    -10^6 <= arr[i] <= 10^6

"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        tmp = sorted(arr)
        _min = tmp[-1] - tmp[0]
        res = []


        for i in range(len(tmp) - 1):
            x, y = tmp[i], tmp[i + 1]
            if (_m := (y - x)) < _min:
                _min = _m
                res.clear()
                res.append((x, y))
            elif _m == _min:
                res.append((x, y))

        return res
