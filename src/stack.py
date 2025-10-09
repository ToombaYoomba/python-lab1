from src.constants import Token


def push(st: list[Token], x: Token) -> None:
    """
    Добавляет токен на верх стэка из токенов
    """
    st.append(x)


def pop(st: list[Token]) -> Token:
    """
    Достаёт верних токен из стэка
    Возвращает токен, но при использовании без переменной его просто удаляет
    """
    if not st:
        raise IndexError("pop from empty stack")
    return st.pop()


def peek(st: list[Token]) -> Token:
    """
    Позволяет посмотреть верхний токен из стэка
    Не меняет стек
    Возвращает верхний токен
    """
    if not st:
        raise IndexError("peek from empty stack")
    return st[-1]


def is_empty(st: list[Token]) -> bool:
    """
    Проверяет, если стэк пустой
    Возвращает булевое значение 1 или 0
    """
    return not st