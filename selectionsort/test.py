import main
import unittest


class test(unittest.TestCase):
    def test_selectionsort(self):
        self.assertEqual(main.selectionSort([5, 3, 7, 1, 2], 5), [1, 2, 3, 5, 7])
        self.assertEqual(main.selectionSort([6, 2, 3, 9, 7, 1], 6), [1, 2, 3, 6, 7, 9])
        self.assertEqual(main.selectionSort([1, 7, 5, 3], 4), [1, 3, 5, 7])
        self.assertEqual(main.selectionSort([7, 8, 4, 9, 2], 5), [2, 4, 7, 8, 9])



if __name__ == '__main__':
    unittest.main()


