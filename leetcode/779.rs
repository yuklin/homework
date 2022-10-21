/* https://leetcode.cn/problems/k-th-symbol-in-grammar/
*
* 779. 第K个语法符号
我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）


示例 1:

输入: n = 1, k = 1
输出: 0
解释: 第一行：0
示例 2:

输入: n = 2, k = 1
输出: 0
解释:
第一行: 0
第二行: 01
示例 3:

输入: n = 2, k = 2
输出: 1
解释:
第一行: 0
第二行: 01


提示:

1 <= n <= 30
1 <= k <= 2n - 1
通过次数48,339提交次数97,222

*/

impl Solution {
    pub fn kth_grammar(n: i32, k: i32) -> i32 {
        let mut kk = k - 1;
        let mut count = 0;

        loop {
            if kk <= 0 {
                break;
            }
            if kk & 1 == 1 {
                count += 1;
            }
            kk = kk >> 1;
        }

        if count & 1 == 1 {
            1
        } else {
            0
        }
    }
}
