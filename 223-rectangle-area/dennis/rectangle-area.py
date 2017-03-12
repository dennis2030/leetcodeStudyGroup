#!/usr/bin/env python2.7
class Solution(object):
    def computeRectangle(self, A, B, C, D):
        if (C - A) < 0 or (D - B) < 0:
            return 0
        return (C - A) * (D - B)
    def computeArea(self, A, B, C, D, E, F, G, H):
        union = self.computeRectangle(A, B, C, D) + self.computeRectangle(E, F, G, H)
        bot_left_x = max(A, E)
        bot_left_y = max(B, F)
        top_right_x = min(C, G)
        top_right_y = min(D, H)
        intersect = self.computeRectangle(bot_left_x, bot_left_y, top_right_x, top_right_y)

        return union - intersect
        

sol = Solution()
sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)

