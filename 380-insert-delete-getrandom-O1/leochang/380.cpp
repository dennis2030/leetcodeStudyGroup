class RandomizedSet {
public:
	/** Initialize your data structure here. */
	RandomizedSet() {
	}

	/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
	bool insert(int val) {
		if (hashMap.find(val) != hashMap.end()){
			return false;
		}

		hashMap[val] = idx.size();
		idx.emplace_back(val);

		return true;
	}

	/** Removes a value from the set. Returns true if the set contained the specified element. */
	bool remove(int val) {
		if (hashMap.find(val) == hashMap.end()){
			return false;
		}

		int del_idx = hashMap[val];
		int last_val = idx.back();
		idx.pop_back();
		hashMap.erase(val);

		if (del_idx < idx.size()) {
			idx[del_idx] = last_val;
			hashMap[last_val] = del_idx;
		}

		return true;
	}

	/** Get a random element from the set. */
	int getRandom() {
		return idx[rand() % idx.size()];
	}
private:
	vector<int> idx;
	unordered_map<int, int> hashMap;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
