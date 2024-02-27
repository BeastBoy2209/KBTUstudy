#1
list1=[]
a=input().split()
for i in a:
    list1.append(int(i))
mult = 2
list2 = list(map(lambda x: x * mult, list1))
print(list2)
#2
s = input("Enter a string: ")

def count_case(s):
    upper, lower = 0, 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower
upper, lower = count_case(s)
print("Upper:", upper)
print("Lower:", lower)
#3
s = input()
def isPalindrome(word):
    print(''.join(reversed(word)))
    if word == reversed(word):
        return True
    else:
        return False
print(isPalindrome(s))
#4
import time
import math

num = int(input())
mil = int(input())

def sqrt_after_mill(number, milliseconds):
    seconds = milliseconds / 1000
    time.sleep(seconds)
    result = math.sqrt(number)
    return result

result = sqrt_after_mill(num, mil)
print(f"Square root of {num} after {mil} milliseconds is {result:.15f}")
#5
tuple1 = (True, 1, "a")

def all_elements_true(tuple1):
    return all(tuple1)

result = all_elements_true(tuple1)
print(result)
if result:
    print("All elements in the tuple are true.")
else:
    print("Not all elements in the tuple are true.")

