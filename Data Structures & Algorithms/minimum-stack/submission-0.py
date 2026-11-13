class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []
        self.min_idx = -1
        self.top_idx = -1

    def push(self, val: int) -> None:
        self.data.append(val)
        self.top_idx += 1

        if self.min_idx >= 0:
            self.mins.append(min(val, self.mins[self.min_idx]))

        else:
            self.mins.append(val)

        self.min_idx += 1

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()
        self.top_idx -= 1
        self.min_idx -= 1


    def top(self) -> int:
        return self.data[self.top_idx]

    def getMin(self) -> int:
        return self.mins[self.min_idx]
