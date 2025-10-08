from src.constants import Token
from src.Errors import CalcError



def calc(a: Token, b: Token, m: Token) -> Token:
    x: float = a[1]
    y: float = b[1]
    op = m[0]
    ans: float = None

    if op == "+":
        ans = x + y

    elif op == "-":
        ans = x - y

    elif op == "*":
        ans = x * y

    elif op == "**":
        ans = x**y

    elif op in "//%":
        if y == 0:
            raise CalcError("Деление на ноль? Да я тебя сейчас на 0 поделю!")
        elif op == "/":
            ans = x / y
        elif op in "//%":
            if x % 1 == 0 and y % 1 == 0:
                if op == "//":
                    ans = x // y
                elif op == "%":
                    ans = x % y

            else:
                raise CalcError(f"Использование {op} не с целыми числами {x} и {y}")

    if ans is None:
        raise CalcError("Использование несуществующей операции", op)

    ans_token: Token = ("NUM", float(ans))

    return ans_token