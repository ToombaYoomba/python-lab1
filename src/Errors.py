from src.constants import Token

class CalcError(Exception):
    """Понятные ошибки калькулятора."""

    pass

def check_mistakes(exp: list[Token]) -> None:
    
    brck_l_example: Token = ("(", None)
    brck_r_example: Token = (")", None)

    if exp == []:
        raise CalcError("Пустой ввод токенов при вереводе в польскую")

    if exp.count(brck_l_example) != exp.count(brck_r_example):
        raise CalcError("Не совпадает количество открывающих и закрвывающих скобок")

    exp_no_brck = exp.copy()

    for item in exp:
        if item[0] in "()":
            exp_no_brck.remove(item)

    if len(exp_no_brck) < 2:
        raise CalcError("Слишком мало операндов или операций")

    if exp_no_brck[0][0] != "NUM" or exp_no_brck[-1][0] != "NUM":
        raise CalcError("Должно начинаться и заканчиваться на число")

    for i in range(len(exp_no_brck) - 1):
        if exp_no_brck[i][0] == exp_no_brck[i + 1][0]:
            raise CalcError("Подряд две операции или операнда")