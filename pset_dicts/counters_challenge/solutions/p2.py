"""
Summing Dict Values - SOLUTION
"""

# Two Kindergarten teachers poll their classes for what fruit they want to eat for snacktime tomorrow. Only one of them is going shopping, so she needs to know how many of each fruit she needs to buy in total. Tally these up and assign them to the "shopping_list" dict.

from collections import Counter

poll1 = {'apples': 8, 'bananas': 12}
poll2 = {'apples': 6, 'bananas': 6, 'clementines': 8}

shopping_list = Counter(poll1) + Counter(poll2)
# print(final_tally) # Counter({'bananas': 18, 'apples': 14, 'clementines': 8})
