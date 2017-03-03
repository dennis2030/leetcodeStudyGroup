/**
 *  * Return an array of size *returnSize.
 *   * Note: The returned array must be malloced, assume caller calls free().
 *    */
int* majorityElement(int* nums, int numsSize, int* returnSize) {
	int *ans = NULL;
	int n = 0;
	int n1 = 0, n2 = 0;
	int ans1 = nums[0], ans2 = nums[0];
	int i = 0;

	for (i = 0; i < numsSize; ++i) {
		if (nums[i] == ans1) {
			n1++;
		} else if (nums[i] == ans2) {
			n2++;
		} else if (0 == n1) {
			ans1 = nums[i];
			n1++;
		} else if (0 == n2) {
			ans2 = nums[i];
			n2++;
		} else {
			if (ans1 != nums[i]) {
				n1--;
			}
			if (ans2 != nums[i]) {
				n2--;
			}
		}
	}

	n1 = 0;
	n2 = 0;

	for (i = 0; i < numsSize; ++i) {
		if (ans1 == nums[i]) n1++;
		else if (ans2 == nums[i]) n2++;
	}

	if (n1 > numsSize / 3 && n2 > numsSize / 3) n = 2;
	else if (n1 > numsSize / 3) n = 1;
	else if (n2 > numsSize / 3) {
		n = 1;
		ans1 = ans2;
	}

	*returnSize = n;
	if (0 < n) {
		ans = malloc(sizeof(int) * n);
		ans[0] = ans1;
		if (1 < n) {
			ans[1] = ans2;
		}
	}

	return ans;
}
