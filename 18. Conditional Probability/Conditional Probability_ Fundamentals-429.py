## 2. Brief Recap ##

# When rolling a 6-sided die

# The probability of getting a 2.
p_2 = 1/6

# The probability of getting an odd number (1, 3, or 5)
p_odd = 3/6

# The probability of getting a 2 or a 4
p_2_or_4 = 2/6

## 3. Updating Probabilities ##

# While rolling a 6-sided die, we know that the number was less than 5
# Possible outcomes: 1, 2, 3, 4

# The probability of getting a 3
p_3 = 1/4

# The probability of getting a 6
p_6 = 0

# The probability of getting an odd number
p_odd = 1/2

# The probability of getting an even number
p_even = p_odd

## 4. Conditional Probability ##

# A student is randomly selected from a class. All we know is that he was born during winter.
# Assume the winter months are December, January, and February and ignore the fact that these
# three months have different number of days. Find

# The probability that he was born in December
p_december = 1/3

# The probability that he was born in a 31-day month
p_31 = 2/3

# The probability that he was born during summer
p_summer = 0

# The probability that he was born in a month which ends in letter "r"
p_ends_r = 1 / 3

## 5. Conditional Probability Formula ##

# the event that the sum is less than eight
card_b = 21

# the event where the sum is an even number AND the event that the sum is less than eight
card_a_and_b = 9

p_a_given_b = card_a_and_b / card_b

## 6. Example Walkthough ##

p_negative_given_non_hiv = 6 / 30

"""
The test needs a lot more work.
"""

## 7. Probability Formula ##

p_premium_given_chrome = 158 / 2762

p_basic_given_safari = 274 / 1288

p_free_given_firefox = 2103 / 2285

more_likely_premium = 'Chrome' if ((158 / 2762) > (120 / 1288)) else 'Safari'