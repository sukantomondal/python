class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        self.list.pop()
    def top(self):
        return self.list[len(self.list)-1]
    def empty(self):
        return self.list == []
    def size(self):
        return len(self.list)

