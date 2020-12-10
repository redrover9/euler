a = 1
b = 2
even_fib = []
even_fib.append(b)

for i in range(0, 4000000):
    c = a + b
    a = b
    b = c
    if b % 2 == 0:
        even_fib.append(b)

print(even_fib)
even_fib_sum = 0

for j in even_fib:
    even_fib_sum += j

print(even_fib_sum)
