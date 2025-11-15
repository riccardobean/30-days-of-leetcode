# Problem 1768: Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ret_string = ""
        cursor1 = 0
        cursor2 = 0
        while cursor1 < len(word1) and cursor2 < len(word2):
            ret_string += word1[cursor1]
            ret_string += word2[cursor2]
            cursor1 += 1
            cursor2 += 1
        while cursor1 < len(word1):
            ret_string += word1[cursor1]
            cursor1 += 1
        while cursor2 < len(word2):
            ret_string += word2[cursor2]
            cursor2 += 1
        return ret_string