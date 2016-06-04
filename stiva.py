class stiva:
    def __init__(self, nmax):
        self.data = [None]*nmax
        self.v = -1
        self.nmax = nmax
    def isEmpty(self):
        return self.v == -1
    def push(self,e):
        if self.v<self.nmax-1:
            self.v = self.v+1
            self.data[self.v]=e
    def top(self):
        if self.isEmpty() is not True:
            return self.data[self.v]
    def pop(self):
        if self.isEmpty() is not True:
            elem = self.data[self.v]
            self.v = self.v-1
            return elem
class stiva2:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    def push(self,e):
        self.data.append(e)
    def top(self):
        if self.isEmpty is not True:
            return self.data[-1]
    def pop(self):
        if self.isEmpty() is not True:
            return self.data.pop()
    def __repr__(self):
        for i in range(len(self.data)):
            print string(self.data[i]),
s = stiva2()
