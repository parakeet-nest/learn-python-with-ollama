 # Intermediate Python Tutorial

Welcome to this comprehensive intermediate Python tutorial! This guide is designed for programmers who already have a grasp of basic Python syntax and concepts. We will delve into advanced data structures, functional programming, object-oriented programming, advanced functions and modules, iterators and generators, context managers, and exception handling. Each section will include in-depth explanations, complex examples, real-world applications, coding challenges, and best practices.

## 1. Advanced Data Structures

### Collections Module

The `collections` module provides alternatives to built-in container data types such as lists, sets, and dictionaries. These alternatives offer more functionality and are often more efficient.

#### Counter

A `Counter` is a dictionary subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
print(word_counts)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

#### Defaultdict

A `defaultdict` is a dictionary subclass that calls a factory function to supply missing values. This can be very useful for avoiding KeyErrors when accessing keys that do not exist in the dictionary.

```python
from collections import defaultdict

def_dict = defaultdict(int)
def_dict['a'] += 1
print(def_dict['b'])  # Output: 0, because the default value is int(0)
```

#### OrderedDict

An `OrderedDict` is a dictionary subclass that remembers the order in which its contents were inserted. This can be useful for maintaining insertion order or for creating dictionaries where the order of elements matters.

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(list(od.keys()))  # Output: ['a', 'b']
```

### Sets and Frozen Sets

Sets are unordered collections of unique elements. They are useful for membership tests and eliminating duplicate entries from a sequence.

```python
s = {1, 2, 3}
print(3 in s)  # Output: True

fs = frozenset({1, 2, 3})
print(hash(fs))  # Output: hash value of the set
```

### Advanced List and Dictionary Comprehensions

List comprehensions provide a concise way to create lists. Dictionary comprehensions offer a similar syntax for creating dictionaries.

```python
# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary comprehension
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

### Coding Challenge

Write a function that takes a list of words and returns a dictionary where the keys are the words and the values are the counts of each word using `Counter`.

```python
from collections import Counter

def word_count(words):
    return dict(Counter(words))

# Example usage:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_count(words))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
```

## 2. Functional Programming

### Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.

```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

### Map, Filter, and Reduce

#### Map

The `map()` function applies a given function to each item of an iterable (like lists or tuples) and returns a list of the results.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

#### Filter

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

```python
numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

#### Reduce

The `reduce()` function applies a rolling computation to sequential pairs of values in an iterable. It is available from the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

### Decorators

Decorators are a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

### Closures

A closure is a record storing a function along with an environment. A closure allows the function to access variables from the surrounding scope, even when the function is invoked outside that scope.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(5))  # Output: 10
```

### Coding Challenge

Write a decorator that prints the name of the function being called and its arguments.

```python
def print_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_function_name
def greet(name):
    return f"Hello, {name}"

# Example usage:
print(greet("Alice"))
# Output:
# Calling greet with args: ('Alice',), kwargs: {}
# Hello, Alice
```

## 3. Advanced Topics

### Context Managers

Context managers are used to allocate and release resources precisely when you want to. The `with` statement simplifies exception handling by encapsulating the preparation and teardown code.

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContextManager() as manager:
    print("Inside the context")
# Output:
# Entering the context
# Inside the context
# Exiting the context
```

### Generators

Generators are a simple way of creating iterators. They allow you to iterate over data without storing the entire dataset in memory.

```python
def countdown(n):
    print("Starting countdown")
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)
# Output:
# Starting countdown
# 3
# 2
# 1
```

### Coding Challenge

Write a generator function that yields the Fibonacci sequence up to `n` terms.

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci(10):
    print(num)
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
```