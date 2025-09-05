
# Author: Contributor 1
def function1(n: int) -> int:
    """Returns factorial of n."""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return 1 if n == 0 else n * function1(n-1)

def function2():
    # Contributor 2 will implement
    pass

def function3(n: int) -> int:
    """Return the nth Fibonacci number (1-indexed). n must be >= 1."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b if n > 1 else 1

def function4():
    # Contributor 4 will implement
    pass


# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("Math Utilities Project Running...")
    print("Factorial of 5:", function1(5))
    print("10th Fibonacci number:", function3(10))
    # Admin will call all contributed functions here
