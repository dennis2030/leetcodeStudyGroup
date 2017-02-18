int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
	int i = 0;
	int curGas = 0;
	int idx = -1;

	if (NULL == gas || NULL == cost || 0 > gasSize || 0 > costSize || gasSize != costSize) {
		return -1;
	}

	for (i = 0; i < gasSize; ++i) {
		gas[i] -= cost[i];
		if (0 <= gas[i] && -1 == idx) {
			idx = i;
		}
	}

	if (-1 == idx) {
		return -1;
	}

	while (idx < gasSize) {
		curGas = 0;

		for (i = 0; i < gasSize; ++i) {
			curGas += gas[(idx + i) % gasSize];

			if (0 > curGas) {
				break;
			}
		}

		if (i == gasSize) {
			return idx;
		}

		idx += (i + 1);
	}

	return -1;
}
