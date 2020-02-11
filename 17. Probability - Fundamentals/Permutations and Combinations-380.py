## 1. The Rule of Product ##

n_outcomes = 36
p_six_six = 1/36
p_not_five_five = 1 - (1/36)

## 2. Extended Rule of Product ##

total_outcomes = 6 * 6 * 6 * 52
p_666_ace_diamonds = 1/total_outcomes
p_no_666_ace_diamonds = 1 - p_666_ace_diamonds

## 3. Example Walkthrough ##

p_crack_4 = 1/10000
p_crack_6 = 1/1000000

## 4. Permutations ##

def factorial_raw(n):
    product = 1
    for x in range(n):
        product *= x + 1
    return product

permutations_1 = factorial_raw(6)
permutations_2 = factorial_raw(52)

## 5. More About Permutations ##

def permutation_raw(n, k):
    product = 1
    for x in range(k):
        product *= n - x
    return product

perm_3_52 = permutation_raw(52, 3)
perm_4_20 = permutation_raw(20, 4)
perm_4_27 = permutation_raw(27, 4)

## 6. Permutations Formulas ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product


def permutation(n, k):
    return factorial(n) / factorial(n - k)

p_crack_pass = 1 / permutation_raw(127, 16)


## 7. Unique Arrangements ##

# def factorial(n):
#     final_product = 1
#     for i in range(n, 0, -1):
#         final_product *= i
#     return final_product

# def permutation(n, k):
#     numerator = factorial(n)
#     denominator = factorial(n-k)
#     return numerator/denominator

def combination_raw(n, k):
    return permutation_raw(n, k) / factorial_raw(k)

c = combination_raw(52, 5)
p_aces_7 = 1 / c
c_lottery = combination_raw(49, 6)
p_big_prize = 1 / c_lottery
print(p_big_prize)

## 8. Combinations ##

def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product


def combination_raw2(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

combinations = combination_raw2

c_18 = combinations(34, 18)
p_non_Y = 1 - 1 / c_18