import unittest
from io import StringIO
import sys
import all_in_one as all

class TestFunctions(unittest.TestCase):

    def test_get_date_of_birth(self):
        self.assertEqual(all.get_date_of_birth("0004185035083"), "18/04/00")
        self.assertEqual(all.get_date_of_birth("0111224903088"), "22/11/01")
        self.assertEqual(all.get_date_of_birth("9809126723080"), "12/09/98")

    def test_get_gender(self):
        self.assertEqual(all.get_gender("9106236034082"), "Male")
        self.assertEqual(all.get_gender("9402030894089"), "Female")
        self.assertEqual(all.get_gender("0312264983083"), "Female")

    def test_fizzbuzz(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        all.fizzbuzz(20)
        sys.stdout = sys.__stdout__
        expected_output = """1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\n"""
        self.assertEqual(expected_output, text_capture.getvalue())

    def test_find_even_numbers(self):
        self.assertEqual(all.find_even_numbers([1, 2, 3, 4, 5]), (2, 4))
        self.assertEqual(all.find_even_numbers([1, 2, 3, 4, 5, 6]), (2, 4, 6))
        self.assertEqual(all.find_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (2, 4, 6, 8))

    def test_find_odd_numbers(self):
        self.assertEqual(all.find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(all.find_odd_numbers([1, 2, 3, 4, 5, 6]), (1, 3, 5))
        self.assertEqual(all.find_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (1, 3, 5, 7))

    def test_return_list_stats(self):
        self.assertEqual(
            all.return_list_stats([1, 2, 3, 4, 5]),
            {
                "unique_numbers": {1, 2, 3, 4, 5},
                "min": 1,
                "max": 5,
                "average": 3.0,
                "even_numbers": (2, 4),
                "odd_numbers": (1, 3, 5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3,
            },
        )

    def test_draw_triangle_reversed(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        all.draw_triangle_reversed(3)
        sys.stdout = sys.__stdout__ 
        self.assertEqual(text_capture.getvalue(), """1 1 1 \n2 2 \n3 \n""")

    def test_draw_triangle_prime(self):
        text_capture = StringIO()
        sys.stdout = text_capture
        all.draw_triangle_prime(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(
            text_capture.getvalue(),
            """2\n3 5\n7 11 13\n17 19 23 29\n31 37 41 43 47\n""",
        )

    def test_pascal_triangle(self):
        self.assertEqual(all.pascal_triangle(0), [1])
        self.assertEqual(all.pascal_triangle(3), [1, 3, 3, 1])
        self.assertEqual(all.pascal_triangle(5), [1, 5, 10, 10, 5, 1])
        self.assertEqual(all.pascal_triangle(6), [1, 6, 15, 20, 15, 6, 1])


if __name__ == "__main__":
    unittest.main()
