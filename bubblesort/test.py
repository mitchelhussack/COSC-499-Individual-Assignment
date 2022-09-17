import main
import unittest


class test(unittest.TestCase):
    def test_bubblesort(self):
        self.assertEqual(main.bubbleSort([5, 3, 7, 6, 1]), [1, 3, 5, 6, 7])
        self.assertEqual(main.bubbleSort([6, 8, 9, 2, 1, 5]), [1, 2, 5, 6, 8, 9])
        self.assertEqual(main.bubbleSort([9, 3, 2, 6, 7]), [2, 3, 6, 7, 9])
        self.assertEqual(main.bubbleSort([1, 5, 3, 7]), [1, 3, 5, 7])



if __name__ == '__main__':
    unittest.main()
