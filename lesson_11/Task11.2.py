from random import randint

class Math:
    def addition(self, x, y):
        print(x + y)

    def subtraction(self, x, y):
        print(x - y)

    def multiplication(self, x, y):
        print(x * y)

    def division(self, x, y):
        print(round(x / y, 3))

mathematics = Math()

num_1 = randint(-100, 100)
num_2 = randint(-100, 100)

print(f"{num_1} + {num_2} = ", end="")
mathematics.addition(num_1, num_2)

print(f"{num_1} - {num_2} = ", end="")
mathematics.subtraction(num_1, num_2)

print(f"{num_1} x {num_2} = ", end="")
mathematics.multiplication(num_1, num_2)

print(f"{num_1} ÷ {num_2} = ", end="")
try:
    mathematics.division(num_1, num_2)
except ZeroDivisionError:
    print("На ноль делить нельзя")


