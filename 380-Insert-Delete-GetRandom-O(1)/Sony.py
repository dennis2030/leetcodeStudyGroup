from random import randrange
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item_idx_map = dict()
        self.item_arr = list()
        self.real_len = self.used_len = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.item_idx_map:
            return False

        self.item_idx_map[val] = self.used_len
        if self.real_len > self.used_len:
            self.item_arr[self.used_len] = val
            self.used_len += 1
        else:
            self.item_arr.append(val)
            self.real_len = self.used_len = self.used_len + 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.item_idx_map:
            return False

        replace_idx = self.item_idx_map.pop(val)
        if self.used_len - 1 != replace_idx:
            replace_val = self.item_arr[self.used_len - 1]
            self.item_idx_map[replace_val] = replace_idx
            self.item_arr[replace_idx] = replace_val
        self.used_len -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        random_idx = randrange(0, self.used_len)
        return self.item_arr[random_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == '__main__':

    sol = Solution()
    print sol.RandomizedSet(n)