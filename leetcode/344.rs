//https://leetcode.cn/problems/reverse-string/
//344. 反转字符串
//提示
//简单
//808
//相关企业
//编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
//
//不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
//
//
//
//示例 1：
//
//输入：s = ["h","e","l","l","o"]
//输出：["o","l","l","e","h"]
//示例 2：
//
//输入：s = ["H","a","n","n","a","h"]
//输出：["h","a","n","n","a","H"]
//
//
//提示：
//
//1 <= s.length <= 105
//s[i] 都是 ASCII 码表中的可打印字符
//通过次数
//789.2K
//提交次数
//988.2K
//通过率
//79.9%
//
//
impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        s.reverse()
        // or...
        //let mut i = 0;
        //let mut j = s.len() - 1;
        //while i < j {
        //    //let tmp = s[i];
        //    //s[i] = s[j];
        //    //s[j] = tmp;
        //    (s[i], s[j]) = (s[j], s[i]);
        //    i += 1;
        //    j -= 1;
        //}
    }
}
