class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        idx = self.map.pop(val)
        if idx == len(self.array) - 1:
            self.array.pop()
        else:
            tail = self.array.pop()
            self.array[idx] = tail
            self.map[tail] = idx
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
