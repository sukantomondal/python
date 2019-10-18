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
    def show(self):
        print(self.list)
        
class Queue:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.insert(0,item)
    def pop(self):
        self.list.pop(0);
    def empty(self):
        return self.list == []
    def size(self):
        return len(self.list)
    def front(self):
        return self.list[0];
    def show(self):
        print(self.list)

