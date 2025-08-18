
# Project Euler Problem 1: Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def solve_problem_1(limit=1000):

    # Find the sum of all multiples of 3 or 5 below the given limit.

    # Args:
        # limit (int): The upper limit (exclusive)

    # Returns:
        # int: Sum of all multiples of 3 or 5 below the limit

    total = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    # Test with the example
    result_example = solve_problem_1(10)
    print(f"Sum of multiples of 3 or 5 below 10: {result_example}")

    # Solve the actual problem
    result = solve_problem_1(1000)
    print(f"Sum of multiples of 3 or 5 below 1000: {result}")
