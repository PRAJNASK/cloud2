def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# User input
n_terms = int(input("Enter the number of terms: "))

# Generating Fibonacci series
fib_series = fibonacci(n_terms)
print("Fibonacci series:")
print(fib_series)
