def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
