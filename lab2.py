
def numbers(n: int) -> None:
    if n < 0:
        return

    print(n)

    numbers(n-1)


def fib(n: int) -> None:
    if n <= 1:
        return n
    else:
        return(fib(n-2)+fib(n-1))


def power(number: int, n: int) -> int:
    if n <= 1:
        return n
    else:
        return n


def reverse(txt: str) -> str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]


def factorial(n: int) ->int:
    if n <=1:
        return 1
    else:
        return n*factorial(n-1)


def prime(n: int) ->bool:
    if n <=0:
        return True
    elif n%prime(n-1) ==0:
        return False
    else:
        return True

if prime(1) ==True:
    print("Prawda")
else:
    print("Nieprawda")
# print(factorial(4))
# txt = "Sebastian"
# print(reverse(txt))
# n= 10
# for i in range(n):
#     print(fib(i))
# numbers(14)