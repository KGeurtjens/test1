# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = np.sinh(x)
z = np.cosh(x)

# Plot the sinh and cosh functions
plt.figure()

plt.plot(x, y, label="sinh(x)")
plt.plot(x, z, label="cosh(x)")

plt.xlim(-5.0, 5.0)

plt.legend()

plt.xlabel("x")
plt.ylabel("f(x)")

plt.savefig("sinh_cosh.png")
plt.show()


def trigon1(a, b, j):
    t = np.linspace(0, 2*np.pi, 10000)
    x = np.cos(a*t) - np.cos(b*t)**j
    return x


def trigon2(c, d, k):
    t = np.linspace(0, 2*np.pi, 10000)
    y = np.sin(c*t) - np.sin(d*t)**k
    return y


t = np.linspace(0, 2*np.pi, 10000)

# Plot the trigon1 function
plt.figure()

plt.plot(t, trigon1(1, 60, 3))

plt.savefig("trigon1.png")
plt.show()

# Plot the trigon2 function
plt.figure(figsize=(6.0, 6.0))

plt.plot(trigon1(1, 60, 3), trigon2(1, 120, 4))

plt.xlabel("trigon1")
plt.ylabel("trigon2")

plt.savefig("trigon1+2.png")
plt.show()