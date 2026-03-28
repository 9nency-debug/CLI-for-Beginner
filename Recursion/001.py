# n = 4
# product = 1

# for i in range(n): # range(4) -> 0, 1, 2, 3
#     product = product * (i + 1)
# print(product)                

# n! = 1 * 2 * 3 * 4 * 5...* n
# n! = [1 * 2 * 3 * 4 * 5...* n -1] * n
# n! = n * (n - 1)! 

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

print(factorial_iter(5))

# or

# f = factorial_iter(5)
# print(f)

def factorial_recursive(num):
    if num == 1 or num == 0: # base condition
        return 1
    return num * factorial_recursive(num - 1)
f = factorial_recursive(0)
print(f)
# f = factorial_iter(5)
# print(f)