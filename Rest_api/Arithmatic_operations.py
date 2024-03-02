class Arithmatic_operators:

    def __init__(self, a, b):
        # if a and b != float:
        # raise TypeError("Values must be of type  float")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            raise ZeroDivisionError("Cannot divide by zero")


# numbers = Arithmatic_operators(4, 8)
# print("Addition:", numbers.add())
# print("Subtraction:", numbers.sub())
# print("Multiplication:", numbers.multiple())
# print("Division:", numbers.divide())
