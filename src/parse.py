from src.constants import Token, TOKEN_RE
from src.Errors import CalcError


def parse(exp: str) -> list[Token]:
    """
    Парсит строку на токены

    Существуют токены чисел и токены операций
    Всегда парсит знак в плотную к числу, как унарный
    Возвращает строку токенов

    """
    if len(exp) == 0 or len(exp.strip()) == 0:
        raise CalcError("Пустой ввод")

    pos = 0
    out: list[Token] = []

    while pos < len(exp):
        m = TOKEN_RE.match(exp, pos)
        if not m:
            # Покажем "хвост" строки, на котором застряли — это удобно при отладке.
            raise CalcError(f"Некорректный ввод около: '{exp[pos:]}'")

        t = m.group(1)
        pos = m.end()
        # print(t)

        # Если токен начинается с цифры — это число → сразу превращаем в float
        if len(t) > 1:
            if t[1:].isdigit():
                out.append(
                    ("NUM", float(t))
                )  # <-- Вот здесь тот самый ("NUM", float(t))
            else:
                out.append((t, None))

        elif t.isdigit():
            out.append(("NUM", float(t)))
        else:
            out.append((t, None))

    # out.append(("EOF", None))
    return out


# print(parse("1/*1"))
