from src.constants import Token, hierarchy
from src.stack import push, pop, peek, is_empty


def to_polish(exp: list[Token]) -> list[Token]:
    """
    Переводит список токенов в обратную польскую запись


    Проходится по списку токенов (изначальное распаршенное выражение)
    При встрече операнда закидывает его в конечною строку
    При встрече операнда закидывает его в стек, если его приоритет в hyerarchy выше
    Иначе вытесняет его из стека, а вытесненная операция идёт в конечную строку
    При встрече закрывающей скобки выкидывает все операции до первой открывающей скобки
    Потом добавляет все оставшиеся операции в стэке, пока он не is_empty (пустой)
    На выход выдаёт список токенов
    """

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
                        # print(") found")
                        while peek(st)[0] != "(":
                            out.append(peek(st))
                            pop(st)
                            # print(pos, st)
                        pop(st)
                        # print(pos, st)
                elif (
                    hierarchy[m[0]] > hierarchy[peek(st)[0]]):  # нормально ложится по иерархии
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