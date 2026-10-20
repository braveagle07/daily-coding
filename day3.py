def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


num = int(input("Enter an integer: "))

print(
    f"{num} is an Armstrong number"
    if is_armstrong(num)
    else f"{num} is NOT an Armstrong number"
)
