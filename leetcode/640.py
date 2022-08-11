"""
    https://leetcode.cn/problems/solve-the-equation/
    640. 求解方程
    求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。
    
    如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。
    
    题目保证，如果方程中只有一个解，则 'x' 的值是一个整数。
    
    
    
    示例 1：
    
    输入: equation = "x+5-3+x=6+x-2"
    输出: "x=2"
    示例 2:
    
    输入: equation = "x=x"
    输出: "Infinite solutions"
    示例 3:
    
    输入: equation = "2x=x"
    输出: "x=0"
    
    
    提示:
    
    3 <= equation.length <= 1000
    equation 只有一个 '='.
    equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。
    通过次数33,117提交次数73,495
"""

from functools import reduce

class Solution:
    def solveEquation(self, equation: str) -> str:
        l, r = equation.split('=')
        if not l.startswith('-'):
            l = '+' + l

        if not r.startswith('-'):
            r = '+' + r

        def helper(s):
            flags = []

            for c in s:
                if c == '+':
                    flags.append('+')
                elif c == '-':
                    flags.append('-')


            raw = reduce(lambda x, y: x + y, [i.split('-') for i in s.split('+')])
            raw = filter(lambda x: x, raw)

            print(flags, raw)
            real = 0
            x_count = 0
            for f, n in zip(flags, raw):
                print(f, n)
                if 'x' not in n:
                    real += int(n) if f == '+' else -int(n)
                else:
                    print('xxx', n)
                    if len(n) != 1:
                        c = int(n[:-1])
                    else:
                        c = 1
                    x_count += c if f == '+' else -c 


            return real, x_count

        l_meta = helper(l)
        r_meta = helper(r)


        if l_meta[1] == r_meta[1] and r_meta[0] == l_meta[0]:
            return 'Infinite solutions'
        elif l_meta[1] == r_meta[1]:
            return 'No solution'

        else:
            res = int((r_meta[0] - l_meta[0]) / (l_meta[1] - r_meta[1]))
            return f'x={res}'


s = Solution()
print(s.solveEquation("2x+3x-6x=x+2"))
print(s.solveEquation("-x=-1"))

