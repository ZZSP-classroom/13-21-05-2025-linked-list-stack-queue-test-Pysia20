import unittest
from text_editor_2 import *

class tests(unittest.TestCase):
    def test_push(self):
        x = Stack()
        x.push("Damian")
        self.assertEqual(x.lista[0],"Damian")
    
    def test_pop(self):
        x = Stack()
        x.push("Damian")
        x.pop()
        self.assertEqual(len(x.lista),0)
    
    def test_peek(self):
        x = Stack()
        x.push("Damian")
        self.assertEqual(x.peek(),"Damian")

if __name__ == "__main__":
    unittest.main()