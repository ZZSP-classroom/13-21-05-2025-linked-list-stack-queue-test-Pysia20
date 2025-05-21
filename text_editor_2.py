class Stack:
    def __init__(self) -> None:
        self.lista = []

    def push(self, object):
        self.lista.append(object)

    def pop(self):
        if len(self.lista) > 0: 
            return self.lista.pop()

    def peek(self):
        if len(self.lista) > 0:
            return self.lista[len(self.lista) - 1]