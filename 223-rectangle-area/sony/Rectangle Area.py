class Solution(object):
    def computeArea(self, L1, D1, R1, U1, L2, D2, R2, U2):
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
        area = (R1 - L1) * (U1 - D1) + (R2 - L2) * (U2 - D2)

        if L1 >= L2:
            if L1 <= R2:
                Li = L1
                Ri = min(R1, R2)
            else:
                #no intersection
                return area
        else:
            if L2 <= R1:
                Li = L2
                Ri = min(R1, R2)
            else:
                #no intersection
                return area

        if D1 >= D2:
            if D1 <= U2:
                Di = D1
                Ui = min(U1, U2)
            else:
                #no intersection
                return area
        else:
            if D2 <= U1:
                Di = D2
                Ui = min(U1, U2)
            else:
                #no intersection
                return area

        return area - (Ri - Li) * (Ui - Di)



if __name__ == '__main__':
    sol = Solution()
    beginWord = "hit"

    print sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)