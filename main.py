
# Author: Contributor 1
def function1(n: int) -> int:
    """Returns factorial of n."""
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    return 1 if n == 0 else n * function1(n-1)

def function2():
    # Contributor 2 will implement
    pass

def function3():
    # Contributor 3 will implement
    pass

def function4(a: int, b: int) -> int:
    """Returns GCD of two numbers."""
    while b:
        a, b = b, a % b
    return a


# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("Math Utilities Project Running...")
    print("Factorial of 5:", function1(5))
    print("GCD of 48 and 18:", function4(48, 18))
    # Admin will call all contributed functions here

