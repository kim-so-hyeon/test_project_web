class Cal1:
    def __init__(self, x):
        self.x = x
    def getPredict(self):
        a = 2*(self.x)
        return a

class Cal2:
    def __init__(self, x):
        self.x = x
    def getPredict(self):
        b = ((self.x)+4)/2
        return b

class Cal3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPredict(self):
        c = self.x + self.y
        return c

# class Cal4:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def getPredict(self):
#         d = 
#         return d