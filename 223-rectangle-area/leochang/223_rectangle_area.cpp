class Solution {
public:
	int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
		int left = A > E ? A : E;
		int bottom = B > F ? B : F;
		int right = C < G ? C : G;
		int top = D < H ? D : H;
		right = right > left ? right : left;
		top = top > bottom ? top : bottom;
		return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (top - bottom);
	}
};
