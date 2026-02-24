import math

# Ask user to enter function
func_input = input("Enter function f(x) (use 'x' as variable, e.g., x**3 - 4*x - 9): ")

# Define function safely
def f(x):
    return eval(func_input)

# Input bounds
a = float(input("Enter lower bound a: "))
b = float(input("Enter upper bound b: "))

# Input tolerance
tolerance = float(input("Enter tolerance (error limit): "))

# Check if root exists in interval
if f(a) * f(b) >= 0:
    print("Bisection method cannot proceed.")
    print("f(a) and f(b) must have opposite signs.")
else:
    print("\nIteration\t a\t\t b\t\t c\t\t f(c)\t\t Error")

    iteration = 1
    c = a
    previous_c = c

    while True:
        previous_c = c
        c = (a + b) / 2
        error = abs(c - previous_c)

        print(f"{iteration}\t\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")

        if abs(f(c)) < tolerance or error < tolerance:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    print("\nApproximate root =", round(c, 6))
    print("Number of iterations =", iteration)