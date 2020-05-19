# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/oco2peak-find_peak.ipynb (unless otherwise specified).

__all__ = ['gaussian']

# Cell
import numpy as np

# Cell
def gaussian(x, m, b, A, sig):
    """
    Function used to fit gaussian in peak_detection
    :param x: float, input data for curve
    :param m: float, slope of the data
    :param b: float, intercept of the data
    :param A: float, curve amplitude
    :param sig: float, standard deviation of curve
    :return: float
    """
    return m * x + b + A / (sig * (2 * np.pi) ** 0.5) * np.exp(-x ** 2 / (2 * sig ** 2))