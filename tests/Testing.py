from src.constants import Token
from src.parse import parse

a: list[Token] = parse("(())")
print([(("("), None)]*2)

if set([(("("), None)]*2).issubset(a):
    print('yes')

print(parse("1 + 1").remove(parse("1 + 1")[-1]))
print(parse("1 + 1").remove(("NUM", float(1))))