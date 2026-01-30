class TwoSum(object):

    def __init__(self):
        self.dic = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.dic[number] = self.dic.get(number,0)+1
        

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for a in self.dic:
            b = value - a
            if b != a:
                if b in self.dic:
                    return True
            else: # a == b
                if self.dic[b] >= 2:
                    return True
        return False

        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)