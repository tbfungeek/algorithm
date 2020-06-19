'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    charSet = set()
    count = 0
    max_length = 0
    substring_start_index = 0
    for i in range(len(s)):
        charSet.add(s[i])
        count += 1
        #如果发现count大于集合内的数量，说明有重复字符
        if count > len(charSet):

            #charSet记录的是目前最大的长度
            if len(charSet) > max_length:
                max_length = len(charSet)

            #找到当前时刻最长的不重复的字符
            index  = s.find(s[i], substring_start_index)
            #将这次查找的在下一次搜索中剔除
            substring_start_index = index+1
            #重置集合及count数值
            charSet = set(s[index + 1:i + 1])
            count = len(charSet)
            
    #遍历结束后触发一次
    if max_length < len(charSet):
        max_length = len(charSet)

    return max_length

print(lengthOfLongestSubstring("HelloWorld"))


'''
性能最高的解法
'''
def lengthOfLongestSubstring_best(s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i ,ans = 0,0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]],i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans;

print(lengthOfLongestSubstring_best("HelloWorld"))