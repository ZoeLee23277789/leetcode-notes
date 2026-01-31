class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.arr = []
        self.window_sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.arr.append(val)
        self.window_sum += val

        if len(self.arr) > self.size:
            remove = self.arr.pop(0)
            self.window_sum -= remove

        return self.window_sum / len(self.arr)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)