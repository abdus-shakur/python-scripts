class Solution(object):
    def countHomogenous(self, s):
        left = 0
        right = 1
        sum = 1
        while(right<len(s)):
            if s[left]==s[right]:
                sum += right - left + 1
            else:
                sum += 1
                left = right
            right += 1
        return sum % (1000000007)
    print(countHomogenous(object,"avvcccaa"))


        