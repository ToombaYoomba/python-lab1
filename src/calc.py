from src.constants import Token
from src.errors import CalcError


def calc(a: Token, b: Token, m: Token) -> Token:
    """
    Подсчитывает выражение из 2-х операндов и одной операции

    На вход получает два токена операнда и один токен операции
    Проходится по всем существующим операциям, при встрече нужной, выполняет её
    На выход выдаёт токен конечного операнда
    """

    # отделение чисел и операции от токенов
    x: float = a[1]
    y: float = b[1]
    op = m[0]

    # проверка на случай странного ввода пользователем
    if op not in "+-//**%":
        raise CalcError("Использование несуществующей операции", op)

    ans: float = None

    # проходится по всем известным операциям их выоплняет соответствующую
    if op == "+":
        ans = x + y

    elif op == "-":
        ans = x - y

    elif op == "*":
        ans = x * y

    elif op == "**":
        ans = x**y

    elif op in "//%":  # обработка операций деления
        if y == 0:
            raise CalcError("Деление на ноль? Да я тебя сейчас на 0 поделю!")
        elif op == "/":
            ans = x / y
        elif op in "//%":  # обработка целочисленных операций
            if x % 1 == 0 and y % 1 == 0:
                if op == "//":
                    ans = x // y
                elif op == "%":
                    ans = x % y

            else:
                raise CalcError(f"Использование {op} не с целыми числами {x} и {y}")

    ans_token: Token = ("NUM", float(ans))

    return ans_token
