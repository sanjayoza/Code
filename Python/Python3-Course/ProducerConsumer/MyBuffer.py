

class MyBuffer:
    def __init__(self, buffsize):
        self.buffsize = buffsize
        self.buffer = []
        for i in range(buffsize):
            self.buffer.insert(i, 0)
        self.bufindex = 0
        
        
    def __repr__(self):
        return "Current Buffer: {}\nBuffer index: {}" .format(self.buffer, self.bufindex)
        
    def insertBuffer(self, value):
        if self.buffer.count(0) == 0:
            print("BUFFER FULL")
            print(self.buffer)
            return
        if self.bufindex < self.buffsize:
            self.buffer.insert(self.bufindex, value)
            self.bufindex += 1
            print("Producer: {}" .format(value))

        else:
            print("Buffer overflow ....")

    
    def removeBuffer(self):
        empty = True
        for x in self.buffer:
            if x != 0:
                empty = False
                break
        if empty:
            print("BUFFER EMPTY")
            return
            
        if self.bufindex > 0:
            idx = self.bufindex - 1
            if idx  >=  0:
                value = self.buffer.pop(idx)
                print("Consumer: {}" .format(value))
                self.bufindex -= 1
                if len(self.buffer) < self.buffsize:
                    self.buffer.insert(idx, 0)
            else:
                print("Buffer underflow ...")
#                 self.__repr__()
