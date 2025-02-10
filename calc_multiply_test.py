# def num_multiply(a,b):
#     result = a * b
#     return result
# r = num_multiply(5, 5)
# print(r)

# Test 1. Verification of multiplication function
# Positive test

def test_multiply():
    # Define the first number
    a = 2
    # Define the second number
    b = 3
    # Perform the multiplication operation
    multiply = a * b
    # Check if the user gets the expected
    assert multiply == 6