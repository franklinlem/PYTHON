class Fila():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0

normal = Fila()
prioritaria = Fila()
normal.push(45)
normal.push(25)
prioritaria.push(61)
prioritaria.push(80)
prioritaria.push(63)
normal.push(58)
prioritaria.push(76)
prioritaria.push(62)
prioritaria.push(94)
normal.push(55)
normal.push(58)
normal.push(40)

cont = 1
while not normal.empty() and not prioritaria.empty():
    if cont % 3 == 0:
        print(normal.pop())
    else:
        print(prioritaria.pop())
    cont += 1
while not normal.empty():
    print(normal.pop())
while not prioritaria.empty():
    print(prioritaria.pop())