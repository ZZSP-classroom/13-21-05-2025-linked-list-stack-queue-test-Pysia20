import unittest
from hospital_1 import *

class tests(unittest.TestCase):
    def test_enqueue(self):
        x = Queue()
        x.enqueue("Damian")
        self.assertEqual(x.queue[0].name,"Damian")
    
    def test_dequeue(self):
        x = Queue()
        x.enqueue("Damian")
        x.enqueue("Kamil")
        self.assertEqual(x.queue[0].name,"Damian")
        x.dequeue()
        self.assertEqual(x.queue[0].name,"Kamil")
    
    def test_peek(self):
        x = Queue()
        x.enqueue("Damian")
        x.enqueue("Kamil")
        x.dequeue()
        self.assertEqual(x.peek()[0].name,"Kamil")

if __name__ == "__main__":
    unittest.main()