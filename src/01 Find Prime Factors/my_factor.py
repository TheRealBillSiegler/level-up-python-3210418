def get_prime_factors(num):
    factors = []
    div = 2
    while div <= num:
        if num % div == 0:
            factors.append(div)
            num = num // div
        else:
            div += 1
    return factors


if __name__ == "__main__":
    print(get_prime_factors(630))
