class Solution(object):
    def computeRectArea(self, A, B, C, D):
        return (C - A) * (D - B)

    def computeInterLength(self, from1, to1, from2, to2):
        if from1 <= from2 <= to2 <= to1:
            return to2 - from2
        if from2 <= from1 <= to1 <= to2:
            return to1 - from1
        if from1 <= from2 <= to1:
            return to1 - from2
        if from1 <= to2 <= to1:
            return to2 - from1
        return 0

    def computeInterArea(self, A, B, C, D, E, F, G, H):
        return self.computeInterLength(A, C, E, G) * self.computeInterLength(B, D, F, H)

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return self.computeRectArea(A, B, C, D) + self.computeRectArea(E, F, G, H) - self.computeInterArea(A, B, C, D, E, F, G, H)
