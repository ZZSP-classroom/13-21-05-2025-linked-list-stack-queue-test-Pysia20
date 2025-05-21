import unittest

class BasicCase(unittest.TestCase):
    def testSomething(self):
        self.assertEqual(1,1)

if __name__ == "__main__":
    unittest.main()