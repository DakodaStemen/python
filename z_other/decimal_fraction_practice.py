# converts string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n / d
        return ans
    else:
        ans = float(in_string)
        return ans


# Decimal to fraction
def dec_to_frac_test():
    import random
    import math
    # Uses string_frac()
    print("Convert the following decimal to a fraction")
    print("Just use the / to write your fraction")
    places = random.randint(1, 4)
    decimal = round(random.random(), places)
    print(decimal)
    d = 10**places
    n = decimal * d
    ans_in = input("Fraction: ")
    if string_frac(ans_in) == decimal:
        print("Correct! \n")
    else:
        print("Try again")
        print("The answer is ", n, "/", d)


# Fraction to percent
def frac_to_perc_test():
    import random
    print("Convert the following fraction to a percent")
    n = round(random.randint(1, 99))
    d = round(random.randint(2, 200))
    print(n, "/", d)
    percent = round(n / d * 100, 2)
    print("Round your answer to two decimal places")
    ans = float(input("Percent: "))
    if ans == percent:
        print("Correct!")
    else:
        print("Try again")
        print("The answer is ", percent)


# test loop
for a in range(3):
    dec_to_frac_test()
    frac_to_perc_test()
    print(" ")
