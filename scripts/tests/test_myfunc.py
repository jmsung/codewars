import unittest


from scripts.myfunc import (
    sign, lst2num, num2lst,
)


class TestMyFunc(unittest.TestCase):
    def test_sign(self):
        test_data = [
            (2, 1),
            (0, 1),
            (-2.6, -1),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(sign(test_input), test_output)

    def test_num2lst(self):
        test_data = [
            (236, [2, 3, 6]),
            (-702, [-7, 0, -2]),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(num2lst(test_input), test_output)

    def test_lst2num(self):
        test_data = [
            ([2, 3, 6], 236),
            ([-7, 0, -2], -702),
        ]
        for test_input, test_output in test_data:
            self.assertEqual(lst2num(test_input), test_output)
