import unittest
from call_center_4 import *

class tests(unittest.TestCase):
    def test_enqueue(self):
        x = Queue()
        x.enqueue()
        self.assertEqual(x.queue[0].caller_id,0)
    
    def test_dequeue(self):
        x = Queue()
        y = Stack()
        x.enqueue()
        x.dequeue(y)
        self.assertEqual(y.lista[0].caller_id,0)
        y.pop()
        self.assertEqual(len(y.lista),0)
    
    def test_peek(self):
        x = Queue()
        y = Stack()
        x.enqueue()
        self.assertEqual(len(x.peek()),1)
        x.dequeue(y)
        self.assertEqual(len(x.peek()),0)
        self.assertEqual(y.peek().caller_id,0)
        y.pop()
        self.assertEqual(y.peek(),None)

if __name__ == "__main__":
    unittest.main()