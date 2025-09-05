
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

def function4():
    # Contributor 4 will implement
    pass
# Author: Contributor 5
def function5(s: str) -> str:
    """Returns the string reversed."""
    return s[::-1]                             

# Driver (Admin will finalize later)
if __name__ == "__main__":
    print("Math Utilities Project Running...")
    print("Factorial of 5:", function1(5))
    print("Original: hello   → Reversed:", function5("hello"))
    # Admin will call all contributed functions here
