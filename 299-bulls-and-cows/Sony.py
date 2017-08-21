class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a_num = 0
        b_num = 0
        secret_num_dict = dict()
        guess_num_dict = dict()
        for idx in xrange(len(guess)):
            if guess[idx] == secret[idx]:
                a_num += 1
                continue
            if secret[idx] not in secret_num_dict:
                secret_num_dict[secret[idx]] = 1
            else:
                secret_num_dict[secret[idx]] += 1
            if guess[idx] not in guess_num_dict:
                guess_num_dict[guess[idx]] = 1
            else:
                guess_num_dict[guess[idx]] += 1
        for key in guess_num_dict.keys():
            if key in secret_num_dict:
                b_num += min(secret_num_dict[key], guess_num_dict[key])
        return '{0}A{1}B'.format(a_num, b_num)

if __name__ == '__main__':

    sol = Solution()
    secret = "1123"
    guess = "0111"

    print sol.getHint(secret, guess)