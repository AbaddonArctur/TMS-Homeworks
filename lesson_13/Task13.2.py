def sequence_generator(n):
    a = 1
    count = 0
    while count < n:
        yield a
        a += 1
        count += 1
        if count % 3 == 0:
            a = 1

while True:
    try:
        inp = int(input("Введите номер конечного элемента последовательности: "))
        break
    except ValueError:
        print("\nОшибка: Введите целое число!\n")

seq_gen = sequence_generator(inp)

for i, value in enumerate(seq_gen):
    if i < inp - 1:
        print(value, end='-')
    else:
        print(value)