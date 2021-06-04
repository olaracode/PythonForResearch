import numpy as np
import matplotlib.pyplot as plt
import harvard

# plt.plot([0, 1, 4, 9, 16])
# plt.show()
# add legend = legend()
# adjust axes: axis()
# set axis labels: xlabel(), ylabel()
# # save figure
# x = np.linspace(0,10,20)
# y = x**2.0
# y2 = x**1.5
# plt.plot(x, y, "bo-", linewidth=2, markersize=12, label="First")

# plt.plot(x, y2, "gs-", linewidth=2, markersize=12, label="Second")

# plt.xlabel("$X$")

# plt.ylabel("$Y$")

# plt.axis([xmin, xmax, ymin, ymax])

# plt.axis([-0.5,10.5, -5, 105])

# plt.legend(loc="upper left")

# plt.savefig("myplot.pdf")

# plt.show()

# semilogx()

# semilogy()

# loglog()

# x = np.logspace(0,1,10)
#
# y = x**2
# plt.loglog(x,y,"bo-")
# plt.show()
# bo- stands for blue circle, gs stands for green square

# histograms

x = np.random.normal(size=1000)
# plt.hist(x, density=True, bins=np.linspace(-5,5,21))
x = np.random.gamma(2,3,100000)
plt.figure()
plt.subplot(221)
plt.hist(x, bins=30)
plt.subplot(222)
plt.hist(x, bins=30,cumulative=True)
plt.subplot(223)
plt.hist(x, bins=30,cumulative=True, density=True)
plt.subplot(224)  # subplot(row, column, location of the item)
plt.hist(x, bins=30,cumulative=True, density=True,histtype="step")
plt.show()