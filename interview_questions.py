import math
#1. *******************************REVERSE A STRING:
#example 1
test_string = "hello world"
reversed_string = test_string[::-1]
print(reversed_string)

#example 2
test_string = "TripleTen"
reverse_string = reversed(test_string)
print(reverse_string)
# convert object to string with join() method
convert_object_to_string = ''.join(reverse_string)
print(convert_object_to_string)

#example 3 for loop
test_string = "loop"
reverse_test_string = reversed(test_string)
new_string = ''
for r in reverse_test_string:
    new_string = new_string + r
print(new_string)

#******Create a function and then test it:********

# Function that reverses a string
def reverse_string(word):
    return ''.join(reversed(word))


# Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "TripleTen"

    # Perform the reverse operation
    reversed_str = reverse_string(input_str)

    # Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"

    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)


def test_reverse_it():
    word = "Breanna"
    reverse_word = reverse_string(word)
    assert reverse_word == "annaerB"
    print("Test Passed!" + word  + "backwards is" + reverse_word)

#2. *******************************CHECK IF PALINDROME:
#Wrote below function/test WITHOUT help
#Function to check if palindrome
def check_palindromes(word):
    reverse_word = ''.join(reversed(word))
    if reverse_word == word:
        return True
    else:
        return False
check_palindromes('kayak')
#Test. Verification of check_palindromes() function
def test_check_palindromes():
    result = check_palindromes('kayak')
    assert result == True

#TripleTen guide
#Function to check if palindrome
def is_palindrome(word):
     reversed_str = ''.join(reversed(word))
     return word == reversed_str
#Test. Verification of test_is_palindrome() function
def test_is_palindrome():
    input_string = 'kayak'
    result = is_palindrome(input_string)
    assert result == True
    print("Test Passed! '" + input_string + "' is a palindrome.")
    #testing Github config

#3. *******************************CALCULATE FACTORIAL OF NUMBER:
#import math to be able to use factorial functionality
#Function to calculate factorial of number
def calc_factorial(number):
    return math.factorial(number)
#Test. Verification of calc_factorial() function
def test_calc_factorial():
    input_num = 5
    result = calc_factorial(input_num)
    assert result == 120
    print("Test Passed! " + str(input_num) + "'s factorial is " + str(result))

