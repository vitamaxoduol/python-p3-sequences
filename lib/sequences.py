#!/usr/bin/env python3

# list = [0, 1, 1, 2, 3, 5, 8, 13, 21]

def print_fibonacci(length):
    a, b = 0, 1
    fibonacci = []
    
    for _ in range(length):
        fibonacci.append(a)
        a, b = b, a + b
    
    print(fibonacci)
        
print(print_fibonacci(9)) 
    