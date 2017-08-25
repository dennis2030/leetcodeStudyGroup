class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        def countExactCorrect(str1, str2):
            assert len(str1) == len(str2)
            count = 0
            for idx in range(len(str1)):
                if str1[idx] == str2[idx]:
                    count += 1
            return count

        def countAlmostCorrect(str1, str2):
            assert len(str1) == len(str2)
            list1 = sorted(str1)
            list2 = sorted(str2)
            count = 0
            while list1 and list2:
                if list1[0] < list2[0]:
                    list1.pop(0)
                elif list1[0] > list2[0]:
                    list2.pop(0)
                else:
                    count += 1
                    list1.pop(0)
                    list2.pop(0)
            return count

        bulls = countExactCorrect(secret, guess)
        cows = countAlmostCorrect(secret, guess) - bulls
        return '{}A{}B'.format(bulls, cows)
