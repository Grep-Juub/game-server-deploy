import unittest

class Testing(unittest.TestCase):
    def dummy_test(self):
        a = 'game'
        b = 'game'

        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()


