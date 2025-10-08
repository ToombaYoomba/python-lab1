from src.calc_polish import calc_polish
from src.parse import parse
from src.to_polish import to_polish


def main() -> None:
    expression = input()

    pa = parse(expression)
    print(f"\nпарсинг: {parse(expression)} \n")

    polish = to_polish(pa)
    print(f"перевод в польскую: {polish} \n")

    ans = calc_polish(polish)
    print(ans)


if __name__ == "__main__":
    main()
