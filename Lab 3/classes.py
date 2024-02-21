import math

#1---------------------------------------------------------------------------------------------------
class MyClass:
    def __init__(self):
        self.my_string = ""

    def getString(self):
        self.my_string = input("Please enter a string: ")

    def printString(self):
        print(self.my_string.upper())

#2---------------------------------------------------------------------------------------------------
class Shape:
    def __init__(self):
        self.area = 0

    def area(self):
        return self.area

class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.area = self.length * self.length

    def area(self):
        return self.area
    
# square = Square(5)
# print(square.area())  

#3---------------------------------------------------------------------------------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def area(self):
        return self.area
    
# rectangle = Rectangle(5, 4)
# print(rectangle.area())  
#4---------------------------------------------------------------------------------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

# p1 = Point(1, 2)
# p2 = Point(4, 6)
# print(p1.show())  
# p1.move(3, 4)
# print(p1.dist(p2)) 

#5 ---------------------------------------------------------------------------------------------------
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return self.balance
# account = Account('John Doe', 1000)
# print(account.deposit(500))  
# print(account.withdraw(200))  
# print(account.withdraw(2000))
#6---------------------------------------------------------------------------------------------------  
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)

