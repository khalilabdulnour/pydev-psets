"""
66. How to replace both the diagonals of dataframe with 0?
"""
"""
Difficulty Level: L2
"""
"""
Replace both values in both diagonals of df with 0.
"""
"""
Input
"""
"""
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))
df
#     0   1   2   3   4   5   6   7   8   9
# 0  11  46  26  44  11  62  18  70  68  26
# 1  87  71  52  50  81  43  83  39   3  59
# 2  47  76  93  77  73   2   2  16  14  26
# 3  64  18  74  22  16  37  60   8  66  39
# 4  10  18  39  98  25   8  32   6   3  29
# 5  29  91  27  86  23  84  28  31  97  10
# 6  37  71  70  65   4  72  82  89  12  97
# 7  65  22  97  75  17  10  43  78  12  77
# 8  47  57  96  55  17  83  61  85  26  86
# 9  76  80  28  45  77  12  67  80   7  63
"""
"""
Desired output
"""
"""
#     0   1   2   3   4   5   6   7   8   9
# 0   0  46  26  44  11  62  18  70  68   0
# 1  87   0  52  50  81  43  83  39   0  59
# 2  47  76   0  77  73   2   2   0  14  26
# 3  64  18  74   0  16  37   0   8  66  39
# 4  10  18  39  98   0   0  32   6   3  29
# 5  29  91  27  86   0   0  28  31  97  10
# 6  37  71  70   0   4  72   0  89  12  97
# 7  65  22   0  75  17  10  43   0  12  77
# 8  47   0  96  55  17  83  61  85   0  86
# 9   0  80  28  45  77  12  67  80   7   0
"""

# Input
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))

# Solution
for i in range(df.shape[0]):
    df.iat[i, i] = 0
    df.iat[df.shape[0]-i-1, i] = 0