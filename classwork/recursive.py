""""an example of recursive functions"""


def factorial(n: int) -> int:
    """Compute the factorial of n"""
    # Base Case
    if n == 0 or n == 1:
        return 1
    else:
        # recursive case
        return n * factorial(n - 1)
