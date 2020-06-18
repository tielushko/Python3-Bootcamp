class Counter:
    def __init__(self, high, low = 0):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for n in Counter(55):
    print(n)