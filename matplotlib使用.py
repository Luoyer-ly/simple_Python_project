# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:27:59 2016

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
pl.plot(x, y,'o')
plt.show()