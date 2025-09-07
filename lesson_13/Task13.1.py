def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        count += 1
        a, b = b, a + b

while True:
    try:
        inp = int(input("Введите номер конечного элемента последовательности: "))
        break
    except ValueError:
        print("\nОшибка: Введите целое число!\n")

fib_gen = fibonacci_generator(inp)

for i in fib_gen:
    print(i, end=' ')