def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    charSet = set()
    count = 0
    max_length = 0
    for i in range(len(s)):
        charSet.add(s[i])
        count += 1
        if count > len(charSet):
            if len(charSet) > max_length:
                max_length = len(charSet)
            charSet.clear()
            charSet.add(s[i])
            count = 1

    if max_length < len(charSet):
        max_length = len(charSet)
        
    print(max_length)

lengthOfLongestSubstring("")