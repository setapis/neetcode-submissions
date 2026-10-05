class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = ''.join(sorted(s))  # 'aaabnn'
        sorted_t = ''.join(sorted(t))
        
        if sorted_s == sorted_t:
            return True
        else:
            return False