from src.constants import Token, TOKEN_RE
from src.errors import CalcError


def parse(exp: str) -> list[Token]:
    """
    Парсит строку на токены

    Существуют токены чисел и токены операций
    Всегда парсит знак в плотную к числу, как унарный
    Возвращает строку токенов

    """
    if len(exp) == 0 or len(exp.strip()) == 0:  # проверка на случай пустой строки
        raise CalcError("Пустой ввод")

    pos = 0
    out: list[Token] = []  # выходной список токенов

    while pos < len(exp):
        m = TOKEN_RE.match(exp, pos)
        if not m:
            # Покажем "хвост" строки, на котором застряли — это удобно при отладке. На случай неизвестного знака
            raise CalcError(f"Некорректный ввод около: '{exp[pos:]}'")

        t = m.group(1)
        pos = m.end()
        # print(t)

        # обратботка знака с длиной больше одного
        if len(t) > 1:
            if t.isdigit() or t[1:].isdigit:  # число с унарным знаком
                out.append(("NUM", float(t)))  # токен числа
            else:  # операции // **
                out.append((t, None))
                

        elif t.isdigit():  # обычное число
            out.append(("NUM", float(t)))
        else:  # операция + - / * %
            out.append((t, None))

    return out
