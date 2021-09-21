# This file implements a Fibonacci sequence calculator using iteration.
# It is intended as a counterpart to the recursive Fibonacci calculator
# studied in class, which is much easier to read but significantly less
# efficient.

def fibonacci(n):
    # Hardcode the first two digits of the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Temporary storage for the two Fibonacci digits we are
    # currently working on. Start with the first 2 digits
    n0 = 0
    n1 = 1

    # Running total
    total = 0

    while n > 0:
        # Calculate the current total
        total = n0 + n1

        # Shift over our temporary variables:
        # For example:
        #
        #            Before:
        #       1      2       3
        #      n0     n1     total
        #
        #            After:
        #       2      3       5   ( 5 = 2 + 3)
        #      n0     n1     total
        n0 = n1
        n1 = total

        # We now have 1 less Fibonacci number to find
        n = n - 1

    return total

print(fibonacci(10000))
