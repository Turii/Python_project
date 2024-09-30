import random


def sum_sum(a, b):
    return a + b


sum_squar = lambda x, y: x ** 2 + y ** 2
print(sum_squar(3, 4))


def sum_squar(x, y):
    return x ** 2 + y ** 2


print(sum_squar(1, 1))

a = "/counterparties/"
b = "/is_issues_certificates_only/"


def cert_only(param):
    return f"/counterparties/{param}/is_issues_certificates_only/"


cert = lambda x: f"/counterparties/{x}/is_issues_certificates_only/"

print(a + "3" + b)
print(cert(3))
print(cert_only(3))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0,1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def ffibon(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return ffibon(n - 1) + ffibon(n - 2)


def ffibfac(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def generate_random_list(n):
    return [random.randint(1, n) for _ in range(n)]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array[1:] if x <= pivot]
        greater_than_pivot = [x for x in array[1:] if x > pivot]
        return quick_sort(less_than_pivot) + pivot + quick_sort(greater_than_pivot)

array = (1, 4, 2, 4456, 3, 7, 8, 20)
print(array)
print(bubble_sort(array))
print(quick_sort(array))
