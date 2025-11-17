# Problem 1071: Greatest Common Divisor of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ret_string = ""
        if len(str1) <= len(str2):
            for char in str1:
                if char in str2 and char not in ret_string:
                    ret_string += char
        else:
            for char in str2:
                if char in str1 and char not in ret_string:
                    ret_string += char

        return ret_string

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))