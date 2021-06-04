import harvard
import math

# random.seed(1) # Fixes the see of the random number generator.
#
# def rand():
#     x = random.uniform(-1.0, 1.0)
#     return x
#
#
# print(rand())
#
# def distance(x, y):
#     distance = math.sqrt((x[1] - y[0])**2 + (y[1] - x[0]) **2)
#     return distance
#
#
# x = distance([0, 0], [1, 1])
# print(x)
#
# random.seed(1)
#
#
# def in_circle(x, origin=[0, 0]):
#     indistance = distance(x, origin)
#     if indistance < 1:
#         return True
#     else:
#         return False
#
#
# in_circle([1, 1])
#
# print("This doesnt make sense")
# r = 10000
# inside = []
# while len(inside) < r:
#     e = in_circle([rand(), rand()])
#     if e is True:
#         inside.append(True)
#     else:
#         inside.append(False)
# print(inside)
# xq = inside.count(True)/r
# pi = math.pi/4
#
# print(pi-xq)
#
#

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors * 2 + 1
    x1 = [x[0]] * n_neighbors + x + [x[-1]] * n_neighbors

    for i in range(n):
        x[i] = sum(x1[i:(i + width)]) / width
    return x
x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))
print(sum(moving_window_average(x,1)))

r = 1000
mh = []

harvard.seed(1)


while len(mh) < r:
    mh.append(harvard.uniform(0, 1))
print(moving_window_average(mh, 5))
