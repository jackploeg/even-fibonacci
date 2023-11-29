from evenfibonacci import FibonacciCalculator
import unittest

class Testing(unittest.TestCase):

    test_limit = 12345

    def setUp(self):
        self.fibonacci_calculator = FibonacciCalculator(self.test_limit)

    def test_init_assigns_correct_upper_limit(self):
        self.assertEqual(self.test_limit, self.fibonacci_calculator.upper_limit)

    def test_init_resets_cache(self):
        self.assertEqual({0:0, 1:1}, self.fibonacci_calculator.cache)

    def test_calculate_value_for_first_10(self):
        expected_values = [0,1,1,2,3,5,8,13,21,34]
        for index in range(0, len(expected_values)):
            self.assertEqual(expected_values[index], self.fibonacci_calculator.calculate_fibonacci_value(index))

    def test_fill_cache_for_50_numbers(self):
        self.fibonacci_calculator.calculate_fibonacci_value(50)
        self.assertEqual(51, len(self.fibonacci_calculator.cache))
        self.assertEqual(12586269025, self.fibonacci_calculator.cache[50])

    def test_fill_cache_to_upper_limit(self):
        self.fibonacci_calculator.fill_cache_to_upper_limit(5000)
        self.assertEqual(20, len(self.fibonacci_calculator.cache))
        self.assertLess(self.fibonacci_calculator.cache[len(self.fibonacci_calculator.cache)-1], 5000)

    def test_sum_even_values(self):
        self.fibonacci_calculator.cache = {0: 0, 1: 1, 2: 2, 3: 18, 4:47, 5:88}
        self.assertEqual(108, self.fibonacci_calculator.sum_even_values_in_cache())

if __name__ == '__main__':
    unittest.main()