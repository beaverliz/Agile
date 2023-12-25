import unittest
from compare_numbers import compare_two_numbers, compare_many_numbers

class TestCompareFunctions(unittest.TestCase):

    def test_compare_two_numbers_position_match(self):
        m = 12345
        n = 12456

        result1, result2 = compare_two_numbers(m, n)

        self.assertEqual(result1, 4)  # Ожидается совпадение в 4 позициях
        self.assertEqual(result2, 2)  # Ожидается 2 совпадения по значению

    def test_compare_two_numbers_no_match(self):
        m = 12345
        n = 67890

        result1, result2 = compare_two_numbers(m, n)

        self.assertEqual(result1, 0)  # Ожидается отсутствие совпадений
        self.assertEqual(result2, 0)  # Ожидается отсутствие совпадений по значению

    def test_compare_many_numbers(self):
        number = 12345
        numbers = [67890, 12456, 54321]

        x_list, y_list = compare_many_numbers(number, *numbers)

        expected_x = [0, 4, 1]  # Ожидаемые значения совпадений по позиции
        expected_y = [0, 2, 2]  # Ожидаемые значения совпадений по значению

        self.assertEqual(x_list, expected_x)
        self.assertEqual(y_list, expected_y)

if __name__ == '__main__':
    unittest.main()
