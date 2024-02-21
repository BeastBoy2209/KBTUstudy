#1
def squareGen():
    N = input()
    N = int(N)
    counter = 0
    while (N > counter):
        print((counter+1)*(counter+1))
        counter +=1
# squareGen()
#2
def evennumGen():
    n = input("Введите число: ")
    n = int(n)
    last_even = None
    for i in range(n + 1):
        if i % 2 == 0:
            if last_even is not None:
                print(",", end="")
            print(i, end="")
            last_even = i
    print()
# evennumGen()
#3
def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = input()
n = int(n)
for number in divisible_by_3_and_4(n):
    print(number)

#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = input()
a = int(a)
b = input()
b = int(b)
for i in squares(a, b):
    print(i)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = input()
n = int(n)
for number in countdown(n):
    print(number)

