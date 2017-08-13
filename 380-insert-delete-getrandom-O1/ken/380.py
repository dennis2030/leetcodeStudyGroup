class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []
        self.idx = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.idx:
            return False

        self.idx[val] = len(self.val)
        self.val.append(val)

        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.idx:
            return False

        idx = self.idx[val]
        del self.idx[val]
        tmp = self.val.pop()
        if idx == len(self.val):
            return True

        self.idx[tmp] = idx
        self.val[idx] = tmp

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random

        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()