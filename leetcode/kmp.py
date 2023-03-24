# KMP, string pattern matching algorithm
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


"""
Simple sliding window:

def strStr(self, haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
        
    return -1

"""


def strStr(self, s: str, p: str) -> int:
    if not p:
        return 0

    if len(p) > len(s):
        return -1

    lps = build_lps(p)
    i = j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == len(p):
                return i - len(p)
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# building the longest proper suffix which is also a prefix
def build_lps(s: str) -> list[int]:
    lps = [0] * len(s)
    j, i = 0, 1
    while i < len(s):
        if s[i] == s[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return lps
