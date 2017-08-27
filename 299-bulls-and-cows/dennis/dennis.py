from collections import defaultdict
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        num_a = 0
        num_b = 0
        
        guess_dict = defaultdict(int)
        matched = [False] * len(guess)
        
        # Collect Digits
        for i in xrange(len(secret)):            
            guess_dict[guess[i]] += 1
        
        # Find all A's
        for i in xrange(len(secret)):            
            secret_digit = secret[i]
            if secret_digit == guess[i]:
                matched[i] = True
                num_a += 1
                guess_dict[secret_digit] -= 1
        # Find all B's
        for i in xrange(len(secret)):
            if matched[i]:
                continue
            secret_digit = secret[i]
            if guess_dict[secret_digit] > 0:
                num_b += 1
                guess_dict[secret_digit] -=1
                
        return '{0}A{1}B'.format(str(num_a), str(num_b))
        
            
