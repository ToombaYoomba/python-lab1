from src.constants import Token, hierarchy
from src.Errors import CalcError, check_mistakes
from src.stack import push, pop, peek, is_empty


def to_polish(exp: list[Token]) -> list[Token]:
    check_mistakes(exp)

    pos = 0
    out: list[Token] = []
    st: list[Token] = []

    while pos < len(exp):
        m = exp[pos]

        if m[0] == "NUM":  # аперанд
            out.append(m)
            # print(pos, st, out)

        elif m[0] != "NUM":
            if is_empty(st):  # если пустой стек
                push(st, m)
                # print(pos, st)
            else:  # операция
                if m[0] in "()":  # скобки
                    if m[0] == "(":
                        push(st, m)
                        # print(pos, st)
                    else:
                        print(") found")
                        c: int = 0
                        while peek(st)[0] != "(":
                            out.append(peek(st))
                            pop(st)
                            c += 1
                            # print(pos, st)
                        if c == 0:
                            if exp[pos - 1][0] == "NUM":
                                if exp[pos - 1][1] < 0 and exp[pos - 2][0] == "(":
                                    pass

                                else:
                                    raise CalcError("Отсутствие операндов в скобке")
                        pop(st)
                        # print(pos, st)
                elif (
                    hierarchy[m[0]] > hierarchy[peek(st)[0]]
                ):  # нормально ложится по иерархии
                    push(st, m)
                    # print(pos, st)
                else:  # вытесняет по иерархии
                    out.append(peek(st))
                    pop(st)
                    push(st, m)
                    # print(pos, st)
        # print("check before +1", pos, st)
        pos += 1

    while not is_empty(st):
        out.append(peek(st))
        pop(st)

    return out