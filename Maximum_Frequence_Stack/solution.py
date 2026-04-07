from collections import deque, defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(deque)
        self.max_freq = 0

    def push(self, val) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f

        if f > self.max_freq:
            self.max_freq = f

        self.stacks[f].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()

        self.freq[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
