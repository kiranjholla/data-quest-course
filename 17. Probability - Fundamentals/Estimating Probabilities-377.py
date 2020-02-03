## 2. The Empirical Probability ##

p_tail = (100 - 56) / 100
p_six = 28 / 200
p_odd = 102 / 200
print(p_tail, p_six, p_odd)

## 3. Probability as Relative Frequency ##

p_heads_1 = (300 - 162) / 300
percentage_1 = p_heads_1 * 100

p_heads_2 = (5000 - 2450) / 5000
percentage_2 = p_heads_2 * 100

## 4. Repeating an Experiment ##

# INITIAL CODE
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'
    
probabilities = []
heads = 0

for n in range(1, 10001):
    # Uncomment above and complete code from here
    if coin_toss() == 'HEAD':
        heads += 1
    
    probabilities.append(heads/n)
    
print(probabilities[0:10])
print(probabilities[-10:])


#yo_prob = []
#yo_head = 0
#seed(1)
#for n in range(1, 10000001):
#    # Uncomment above and complete code from here
#    if coin_toss() == 'HEAD':
#        yo_head += 1
#    
#    yo_prob.append(yo_head/n)
#
#yo_prob[-1]

## 5. The True Probability Value ##

p_l = 87 / 200
p_l_and_c = 40 / 200
p_h = 63 / 200
p_no = (200 - 160) / 200

## 6. The Theoretical Probability ##

p_ht = 1 / 4
p_5 = 1 / 6
p_tt = p_ht

## 7. Events vs. Outcomes ##

p_even = 0.5
p_odd_no_3 = 2 / 6
p_odd_greater_5 = 0

## 8. A Biased Die ##

p_blue = 10 / 100
p_red = 90 / 100