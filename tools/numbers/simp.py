class SimpFunctions:
    def __init__(self):
        self.functions_called = set()

    def add(self, x, y):
        self.functions_called.add("add")
        return x + y

    def subtract(self, x, y):
        self.functions_called.add("subtract")
        return x - y
