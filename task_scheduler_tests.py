import unittest
from task_scheduler_5 import *

class tests(unittest.TestCase):
    def test_add(self):
        x = PriorityQueue()
        x.add_task(1,"idk")
        x.add_task(2,"idk3")
        x.add_task(0,"idk2")
        self.assertEqual(x.printLL(),["idk3","idk","idk2"])
    
    def test_process_task(self):
        x = PriorityQueue()
        x.add_task(1,"idk")
        x.add_task(2,"idk3")
        x.add_task(0,"idk2")
        x.process_task()
        self.assertEqual(x.printLL(),["idk","idk2"])

if __name__ == "__main__":
    unittest.main()