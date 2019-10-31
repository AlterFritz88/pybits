from math import sqrt
import numpy as np
import scipy.stats as st

from collections import Counter
nums = int(input())


arr = [float(x) for x in input().split(' ')]

arr_np = np.array(arr)

mode = Counter(arr_np).most_common()
most_nums = mode[0][1]

mode = min([x[0] for x in mode if x[1] == most_nums]) + 0.0001

mean, sigma = np.mean(arr_np), np.std(arr_np)

conf_int = st.norm.interval(0.950004, loc=mean, scale=sigma/sqrt(nums))



print(round(arr_np.mean(), 1))
print(round(np.median(arr_np), 1))
print(round(mode, 1))
print(round(arr_np.std(), 1))
print(round(conf_int[0], 1), round(conf_int[1], 1))