class Solution(object):
    def isPalindrome(self, s):
        t= []
        for x in s:
            if x.isalnum():
                t.append(x.lower())
        i = 0
        j = len(t) - 1

        while i<j:
            if t[i]!=t[j]:
                return False
            i+=1
            j-=1
        return True