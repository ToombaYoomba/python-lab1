from src.constants import Token


def push(st: list[Token], x: Token) -> None:
    st.append(x)


def pop(st: list[Token]) -> Token:
    if not st:
        raise IndexError("pop from empty stack")
    return st.pop()


def peek(st: list[Token]) -> Token:
    if not st:
        raise IndexError("peek from empty stack")
    return st[-1]


def is_empty(st: list[Token]) -> bool:
    return not st