class Solution(object):
    def eliminateFromFront(self, first, last, step):
        if (last - first) % (step * 2) == 0:
            last -= step
        first += step
        return first, last

    def eliminateFromBack(self, first, last, step):
        if (last - first) % (step * 2) == 0:
            first += step
        last -= step
        return first, last

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last, step = 1, n, 1
        direction = 'front'

        while first < last:
            if direction == 'front':
                first, last = self.eliminateFromFront(first, last, step)
                direction = 'back'
            elif direction == 'back':
                first, last = self.eliminateFromBack(first, last, step)
                direction = 'front'
            step *= 2

        return first
