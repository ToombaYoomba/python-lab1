from src.constants import Token

class CalcError(Exception):
    """Понятные ошибки калькулятора."""

    pass

def check_mistakes(exp: list[Token]) -> None:
    """
    Функция, которая проверяет ошибки записанного выражения после парсинга

    Ничего не возвращает, может только возвести ошибку
    """
    
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

    if len(exp_no_brck) < 2 and exp_no_brck[0][0] != "NUM":
        raise CalcError("Слишком мало операндов")

    if exp_no_brck[0][0] != "NUM" or exp_no_brck[-1][0] != "NUM":
        raise CalcError("Должно начинаться и заканчиваться на число")

    for i in range(len(exp_no_brck) - 1):
        if exp_no_brck[i][0] == "NUM" and exp_no_brck[i + 1][0] == "NUM":
            raise CalcError("Подряд два оператора")
        elif exp_no_brck[i][1] is None and exp_no_brck[i + 1][1] is None:
            raise CalcError("Подряд два операнда")
        
    for i in range(len(exp) - 1):
        if exp[i][0] == "NUM" and exp[i + 1][0] == "(":
            raise CalcError("Операнд перед открывающей скобкой")
        elif exp[i][0] == "(" and exp[i + 1][0] in "+-**//%":
            raise CalcError("Оператор после открывающей скобки")
        elif exp[i][0] in "+-**//%" and exp[i + 1][0] == ")":
            raise CalcError("Оператор перед закрывающей скобкой")
        elif exp[i][0] == ")" and exp[i + 1][0] == "NUM":
            raise CalcError("Операнд после закрывающей скобки")
        
        
    