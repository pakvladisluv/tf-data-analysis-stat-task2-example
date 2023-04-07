import pandas as pd
import numpy as np
import math as mt

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 408773855 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = x.shape[0]
    left1 = chi2.ppf(1-alpha/2, 2*n)
    right1 = chi2.ppf(alpha/2, 2*n)
    left = np.sqrt(sum(x**2) / (left1 * 35))
    right = np.sqrt(sum(x**2) / (right1 * 35))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return left, right
