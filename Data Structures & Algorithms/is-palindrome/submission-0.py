class Solution:
    def isAlphaNumeric(self, s):
        return s >= "A" and s <= "Z" or s >= "a" and s <= "z" or s >= "0" and s <= "9"

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if not self.isAlphaNumeric(s[i]):
                i += 1
            elif not self.isAlphaNumeric(s[j]):
                j -= 1
            elif s[i].casefold() == s[j].casefold():
                i += 1
                j -= 1
            else:
                return False
        return True
