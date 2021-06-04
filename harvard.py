import numpy as np
import matplotlib.pyplot as plt
import random
import time
import numpy as np

# coin = ["Heads", "Tails"]
# d1, d2 = range(1, 7), range(1, 7)
# print()
#
# # rolls = []
# # for i in range(1000000):
# #     rolls.append(random.choice(d1))
# #
# ys = []
# for k in range(1000000):
#     y = 0
#     for i in range(10):
#         x = random.choice(d1)
#         y = y + x
#     ys.append(y)
# print(ys)
# print(min(ys), max(ys))
# plt.hist(ys);
# plt.show()
start_time = time.process_time()

print(np.random.randint(0, 5))  # np.random.randint(Lowest number, highest number)

x = np.random.randint(1, 7, (10, 3))
print(np.sum(x, axis=0))  # with the axis parameter you can sum over a single line of the "matrix"
# Measuring time
end_time = time.process_time()
print(end_time - start_time)
