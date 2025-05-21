class Call:
    def __init__(self,caller_id,time_recived):
        self.caller_id = caller_id
        self.time_recived = time_recived

class Queue:
    def __init__(self):
        self.queue = []
        self.time = 0
        self.id = 0
    
    def enqueue(self):
        call = Call(self.id,self.time)
        self.time += 1
        self.queue.append(call)
        return True
    
    def dequeue(self,stack):
        low = self.queue[0].time_recived
        low_index = 0
        current_index = 0

        for i in self.queue:
            if low > i.time_recived:
                low = i.time_recived
                low_index  = current_index
            current_index += 1

        stack.push(self.queue.pop(low_index))
        return True
    
    def peek(self):
        return self.queue
    
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