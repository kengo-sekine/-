"""Check digit calculation logic."""


def calc_check_digit(value: str) -> str:
    """Return the check digit for a 4-digit string."""
    n1, n2, n3, n4 = (int(char) for char in value)

    n5 = 5 * n1 + 4 * n2 + 3 * n3 + 2 * n4
    n5 %= 9

    if n5 % 6 == 0:
        n5 = 1
    else:
        if n5 % 2 == 0:
            n5 //= 2

        if n5 == 1:
            n5 = 0

    return str(n5)


def main(target_list: list[str]) -> None:
    """Print each input value with its check digit appended."""
    for value in target_list:
        print(value + calc_check_digit(value))
