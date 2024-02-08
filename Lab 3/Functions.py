import math
import random
from itertools import permutations
#1
def convert_to_ounces(grams):
    ounces = grams / 28.3495231
    return ounces
#2
def fahrenheit_to_centigrade(f):
    c = (5 / 9) * (f - 32)
    return c
#3
def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return "No solutions!"
#4
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return list(filter(is_prime, numbers))
#5
def print_permutations(s):
    return [''.join(p) for p in permutations(s)]
#6
def reverse_words(s):
    return ' '.join(reversed(s.split()))
#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
#8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
#9
def sphere_volume(r):
    return (4 / 3) * math.pi * r**3
#10
def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst
#11
def is_palindrome(s):
    return s == s[::-1]
#12
def histogram(lst):
    for i in lst:
        print('*' * i)
#13
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break
    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
#14
