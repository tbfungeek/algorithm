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