class FirstUnique:

    def __init__(self, nums):
        self.q = []
        self.d = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        while len(self.q) > 0 and self.d[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value):
        if value in self.d:
            self.d[value] += 1
        else:
            self.d[value] = 1
            self.q.append(value)