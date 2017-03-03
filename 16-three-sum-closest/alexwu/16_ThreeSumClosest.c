int cmp(const void * a, const void * b)
{
	return (*(int*)a -*(int*)b);
}

int threeSumClosest(int* nums, int numsSize, int target) {
	int min_diff = 0;
	int diff = 0;
	int p1 = 0, p2 = 1, p3 = numsSize - 1;
	int i = 0;
	int ans = 0, sum = 0;

	qsort(nums, numsSize, sizeof(int), cmp);
	ans = nums[p1] + nums[p2] + nums[p3];
	min_diff = abs(ans - target);

	for (i = 0; i <= numsSize - 3; ++i) {
		p1 = i;
		p2 = p1 + 1;
		p3 = numsSize - 1;

		do {
			sum = nums[p1] + nums[p2] + nums[p3];
			diff = sum - target;

			if (0 == diff) {
				return target;
			} else if (0 > diff) {
				p2++;
			} else {
				p3--;
			}

			if (abs(diff) < min_diff) {
				ans = sum;
				min_diff = abs(diff);
			}
		} while (1 <= p3 - p2);
	}

	return ans;
}
