import re

Token = tuple[str, float | None]

TOKEN_RE = re.compile(
    r"""
    \s*(
        [+-]?\d+(?:\.\d+)?
        | \*\* 
        | // 
        | [%()+\-*/]
    )""",
    re.VERBOSE,
)


hierarchy = {"+": 1, "-": 1, "*": 2, "/": 2, "//": 2, "%": 2, "**": 3, "(": 0, ")": 0}
