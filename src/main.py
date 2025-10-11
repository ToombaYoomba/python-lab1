from src.calc_polish import calc_polish
from src.errors import check_mistakes
from src.parse import parse
from src.to_polish import to_polish


def main() -> None:
    """
    Основаня функция - калькулятор

    На вход получает выражение строку из терминала
    Парсит его, проверяет на ошибки, переводит в польскую запись и считает
    В итоге печатает ответ
    Ничего не возвращает
    """

    expression = input("Введите математическое выражение: ")  # входное выражение

    pa = parse(expression)  # парсинг
    print(f"\nпарсинг: {parse(expression)} \n")

    check_mistakes(pa)  # проверка ошибок

    polish = to_polish(pa)  # перевод в польскую запись
    print(f"перевод в польскую: {polish} \n")

    ans = calc_polish(polish)  # вычисление выражения
    print(f"Результат вычислений: {ans}")


if __name__ == "__main__":
    main()
