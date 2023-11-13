functions_called = set()

def add(x, y):
    functions_called.add("add")
    return x + y

def subtract(x, y):
    functions_called.add("subtract")
    return x - y