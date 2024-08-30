import unittest

def add(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(sum([6,4]), 7)

if __name__ == '__main__':
     unittest.main()