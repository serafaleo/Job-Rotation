# -*- coding: utf-8 -*-

def num_pertence_a_fib(num):
    if num == 0 or num == 1:
        return True

    fib1 = 0
    fib2 = 1

    fib = fib1 + fib2

    while fib < num:
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2

    if fib == num:
        return True
    else:
        return False

def main():
    num = int(input("Informe um número: "))
    helper_str = "pertence à sequência de Fibonacci."
    if num_pertence_a_fib(num):
        print(f"{num} {helper_str}")
    else:
        print(f"{num} não {helper_str}")

if __name__ == "__main__":
    main()
