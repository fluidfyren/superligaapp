import numpy as np


def update_plot(p):
    x = np.arange(10)
    y = x**1.2
    p.line(x,y)