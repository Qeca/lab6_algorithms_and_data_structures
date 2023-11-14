import unittest
from MySet import MySet


class MySetTestCase(unittest.TestCase):
    def test_init(self):
        ms = MySet(1, 2, 3, 4, 5)
        self.assertEqual(f"{ms}", "[1, 2, 3, 4, 5]")

    def test_add(self):
        ms = MySet()
        a = [1, 23, 43, 4, 3, 4, 34, 2, 34, 24, 2]
        for i in a:
            ms.add(i)
        self.assertEqual(f'{ms}', f'[1, 23, 43, 4, 3, 34, 2, 24]')

    def test_is_empty(self):
        ms = MySet()
        self.assertEqual(ms.is_empty(), True)

    def test_size(self):
        ms = MySet(1, 23, 4)
        self.assertEqual(ms.size(), 3)

    def test_remove_all(self):
        ms = MySet(23, 23, 123, 1, 321, 3, )
        ms.remove_all()
        self.assertEqual(ms.is_empty(), True)

    def test_contains(self):
        ms = MySet(1, 23, 4, 5, 6, 8, 9)
        self.assertEqual(ms.contains(1), True)

    def test_for_each(self):
        ms = MySet(1, 2, 3)
        result = []
        ms.for_each(lambda x: result.append(x))
        self.assertEqual(result, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
