def removePalindrome(s):
    if s == s[::-1]:
        return -1

    n = len(s)
    for i in range(len(s)//2):
        if s[i] != s[n-1-i]:
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                return n-1-i
            if s[i+1:n-1]==s[i+1:n-1][::-1]:
                return i



aababcaa