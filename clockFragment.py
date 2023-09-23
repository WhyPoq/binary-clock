
class ClockFragment:

    def __init__(self):
        self.curNum = 0
        self.bits = [0] * 4
        self.recalc()

    def setNum(self, num):
        if(self.curNum == num):
            return False
        self.curNum = num
        self.recalc()
        return True

    def recalc(self):
        a = self.curNum
        for i in range(4):
            self.bits[i] = a & 1
            a = a >> 1

