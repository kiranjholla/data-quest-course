## 1. Complex Probability Problems ##

p_a = 12 / 100
p_b = 17 / 100
p_a_and_b = 3 / 100
p_a_or_b = p_a + p_b - p_a_and_b

## 2. Opposite Events ##

p_non_basic = 1 - 0.2
p_non_premium = 1 - 0.15

p_subscription = 0.2 + 0.15
p_non_subscription = 1 - p_subscription

## 3. Example Walk-Through ##


# HHH
# HHT
# 
# HTH
# HTT
#
# THH
# THT
# 
# TTH
# TTT

# p_b = 0.5 * 0.5 * 0.5
# p_non_b = 1 - p_b

p_non_b = 7/8
p_b = 1 - p_non_b

## 4. Set Complements ##

p_non_click = 0.5
p_two_or_less = 0.75
p_three_or_more = 0.25

## 5. The Multiplication Rule ##

p_6_6 = 1/6 * 1/6
p_3_2 = p_6_6
p_even_even = 1 / 4
p_1_even = 1/6 * 1/2

## 6. Independent Events ##

p_18h = 0.5 ** 18
p_666 = (1/6) ** 3
p_not_6 = (5/6) ** 4

## 7. Combining Formulas ##

# What is the probability of getting at least one double-six in 24 throws of two six-sided dice
p_one_double_6 = 1 - ((35/36) ** 24)




## 8. Sampling With(out) Replacement ##

# Getting two kings in a row
p_kk = 4/52 * 3/51

# Getting a seven of hearts, followed by a queen of diamonds
p_7q = 1/52 * 1/51

# Getting a jack, followed by a queen of diamonds, followed by a king, followed by another jack
p_jqkj = 4/52 * 1/51 * 4/50 * 3/49