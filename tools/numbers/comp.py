class CompFunctions:
    def __init__(self):
        self.functions_called = set()

    def sum_of_digits(self, num):
        self.functions_called.add("sum_of_digits")
        return sum(int(digit) for digit in str(num))

    def is_palindrome(self, num):
        self.functions_called.add("is_palindrome")
        num_str = str(num)
        return num_str == num_str[::-1]