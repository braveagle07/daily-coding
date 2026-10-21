def is_armstrong(n: int) -> bool:
    """True if n equals the sum of its digits, each raised to the digit count.

    Example: 153 = 1**3 + 5**3 + 3**3. Negative numbers are never Armstrong.
    """
    if n < 0:
        return False
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


def main():
    num = int(input("Enter an integer: "))

    print(
        f"{num} is an Armstrong number"
        if is_armstrong(num)
        else f"{num} is NOT an Armstrong number"
    )


if __name__ == "__main__":
    assert is_armstrong(0) and is_armstrong(9)
    assert is_armstrong(153) and is_armstrong(9474)
    assert not is_armstrong(10) and not is_armstrong(-153)
    main()
