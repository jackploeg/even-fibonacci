import sys

class FibonacciCalculator:

    def __init__(self, upper_limit):
        # Instance variable
        self.upper_limit = upper_limit
        self.cache = self.init_cache()

    def init_cache(self):
        return {0: 0, 1: 1}

    def find_even_fibonacci_numbers(self):
        self.fill_cache_to_upper_limit(self.upper_limit)
        self.sum_even_values_in_cache()

    def calculate_fibonacci_value(self, n):
        if n in self.cache:  # Base case
            return self.cache[n]
        # Compute and cache the Fibonacci number
        self.cache[n] = self.calculate_fibonacci_value(n - 1) + self.calculate_fibonacci_value(n - 2)  # Recursive case
        return self.cache[n]

    def fill_cache_to_upper_limit(self, limit):
        fibonacci_value = 0
        index = 0
        self.cache = self.init_cache()
        # Loop until we find the first Fibonacci number larger than the upper limit
        while fibonacci_value < limit:
            fibonacci_value = self.calculate_fibonacci_value(index)
            index += 1
        # Remove last item from cache because this is larger than the upper limit
        self.cache.pop(index-1)

    def sum_even_values_in_cache(self):
        # Sum the even values in the cache
        sum = 0
        for entry in self.cache:
            if (self.cache[entry] % 2)==0:
                sum += self.cache[entry]
        print("Sum of even Fibonacci numbers smaller than", self.upper_limit, ": ", sum)
        return sum

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # Check if the argument is a digit
        if arg.isdigit():
            # Convert the argument to an integer
            upper_limit = int(arg)
        else:
        # Print an error message
            print("Error: Upper limit argument is not an integer, using default value.")
            upper_limit = 4000000
    else:
        upper_limit = 4000000
    fibonacci_calculator = FibonacciCalculator(upper_limit)
    fibonacci_calculator.find_even_fibonacci_numbers()
