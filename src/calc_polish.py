from src.constants import Token
from src.Errors import CalcError
from src.stack import push, pop
from src.calc import calc


def calc_polish(exp: list[Token]) -> float:
    """
    Считывает список токенов (выражение в польской записи) и даёт ответ к выражению

    На вход получает список токенов
    Проходится по списку и при встрече операнда закидывает его в стэк
    При встрече операции достаёт последние два операнда из стэка
    и производит с ними соответвующее операции действие через функцию calc()
    Результат операции добавляет обратно в стэк
    После прохода по всему выражению оставшийся операнд достаёт из стэка и округляет его значение
    Возвращает округлённое число
    """
    if exp == []:
        raise CalcError("Пустой ввод токенов при подсчёте польской")

    pos = 0
    out: float = None
    st: list[Token] = []

    while pos < len(exp):
        m = exp[pos]

        if m[0] == "NUM":
            push(st, m)
            # print(pos, st)

        elif m[0] != "NUM":
            if len(exp) < 2:
                raise CalcError(
                    "Слишком мало операндов для операции при подсчёте польской"
                )

            else:
                b = pop(st)
                a = pop(st)
                res = calc(a, b, m)
                push(st, res)
                # print(pos, st)

        pos += 1

    out = st[0][1]

    return round(out, 6)
