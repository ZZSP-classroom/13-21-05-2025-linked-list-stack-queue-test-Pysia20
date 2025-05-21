class patient:
    def __init__(self,name,appointment_time) -> None:
        self.name = name
        self.appointment_time = appointment_time

class Queue:
    def __init__(self):
        self.queue = []
        self.time = 0
    
    def enqueue(self,name):
        patientt = patient(name,self.time)
        self.time += 1
        self.queue.append(patientt)
        return True
    
    def dequeue(self):
        low = self.queue[0].appointment_time
        low_index = 0
        current_index = 0

        for i in self.queue:
            if low > i.appointment_time:
                low = i.appointment_time
                low_index  = current_index
            current_index += 1

        self.queue.pop(low_index)
        return True
    
    def peek(self):
        return self.queue
