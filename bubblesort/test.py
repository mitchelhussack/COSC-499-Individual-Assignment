import main
import unittest


class test(unittest.TestCase):
    def test_bubblesort(self):
        result = main.bubbleSort([5, 3, 7, 9, 8])
        self.assertEqual(result, [3, 5, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()