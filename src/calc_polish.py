from src.constants import Token
from src.Errors import CalcError
from src.stack import push, pop
from src.calc import calc



def calc_polish(exp: list[Token]) -> float:
    if exp == []:
        raise CalcError("Пустой ввод токенов")

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
                raise CalcError("Слишком мало операндов для операции")

            else:
                b = pop(st)
                a = pop(st)
                res = calc(a, b, m)
                push(st, res)
                # print(pos, st)

        pos += 1

    out = st[0][1]

    return round(out, 6)