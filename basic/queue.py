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


q = Queue()

q.push(10)

q.show()

q.push("dd")

q.show()

print(q.front())


while q.size() != 0:
    print(q.front())
    q.pop()
        
