def is_prime (func):
    def wrapper(*args):
        number = func(*args)
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return f"Составное число: {number}"
        return f"Простое число: {number}"
    return  wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(3, 3, 6)
print(result)