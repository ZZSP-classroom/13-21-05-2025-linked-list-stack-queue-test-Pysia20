# Create a Task class to create a Task
class Task:
    def __init__(self, priority, task_name):
        self.priority = priority
        self.task_name = task_name
        self.next = None

# Create a PriorityQueue class
class PriorityQueue:
    def __init__(self):
        self.head = None

    # Method to add a Task at begin of LL
    def insertAtBegin(self, priority, task_name):
        new_Task = Task(priority,task_name)
        if self.head is None:
            self.head = new_Task
            return
        else:
            new_Task.next = self.head
            self.head = new_Task


    # Method to add a Task at any index
    # Indexing starts from 0.
    # Method to add a Task at any index
    # Indexing starts from 0.
    def add_task(self, priority, task_name):
        new_task = Task(priority, task_name)

        # If list is empty or new task has higher priority than head
        if self.head is None or self.head.priority < priority:
            new_task.next = self.head
            self.head = new_task
            return

        current = self.head
        # Traverse until we find a node with lower priority or reach end
        while current.next is not None and current.next.priority >= priority:
            current = current.next

        new_task.next = current.next
        current.next = new_task


    # Method to add a Task at the end of LL
    def insertAtEnd(self, priority,task_name):
        new_Task = Task(priority,task_name)
        if self.head is None:
            self.head = new_Task
            return
        current_Task = self.head
        while(current_Task.next):
            current_Task = current_Task.next
        current_Task.next = new_Task

    # Update Task of a linked list
    # at given position
    def updateTask(self, val, index):
        current_Task = self.head
        position = 0
        if position == index:
            current_Task.priority = val
        else:
            while(current_Task != None and position != index):
                position = position+1
                current_Task = current_Task.next
            if current_Task != None:
                current_Task.priority = val
            else:
                print("Index not present")

    # Method to remove first Task of linked list
    def process_task(self):
        if(self.head == None):
            return
        self.head = self.head.next

    # Method to remove last Task of linked list
    def remove_last_Task(self):
        if self.head is None:
            return
        current_Task = self.head
        while current_Task.next.next:
            current_Task = current_Task.next
        current_Task.next = None

    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_Task = self.head
        position = 0
        if position == index:
            self.process_task()
        else:
            while(current_Task != None and position+1 != index):
                position = position+1
                current_Task = current_Task.next
            if current_Task != None:
                current_Task.next = current_Task.next.next
            else:
                print("Index not present")

    # Method to remove a Task from linked list
    def remove_Task(self, priority):
        current_Task = self.head
        while(current_Task != None and current_Task.next.priority != priority):
            current_Task = current_Task.next
        if current_Task == None:
            return
        else:
            current_Task.next = current_Task.next.next

    # print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_Task = self.head
            while(current_Task):
                size = size+1
                current_Task = current_Task.next
                return size
        else:
            return 0

    # print method for the linked list
    def printLL(self):
        listt = []
        current_Task = self.head
        while(current_Task):
            listt.append(current_Task.task_name)
            current_Task = current_Task.next
        return listt