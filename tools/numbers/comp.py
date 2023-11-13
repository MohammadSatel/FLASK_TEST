functions_called = set()

def sum_of_digits(num):
    functions_called.add("sum_of_digits")
    return sum(int(digit) for digit in str(num))

def is_palindrome(num):
    functions_called.add("is_palindrome")
    num_str = str(num)
    return num_str == num_str[::-1]