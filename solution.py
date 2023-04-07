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
    #loc = np.mean(x)
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #left = chi2.ppf(1 - alpha/2, df=len(x))
    #right = chi2.ppf(alpha/2, df=len(x))
    #y = 0
    #for i in range(len(x)):
    #    y = y + x[i]**2
    #left = norm.ppf(1 - alpha/2, df=len(x))
    #right = norm.ppf(alpha/2, df=len(x))
    left1 = chi2.ppf(1-alpha/2, 2*n)
    right1 = chi2.ppf(alpha/2, 2*n)
    left = np.sqrt(sum(x**2) / left1 * 35)
    right = np.sqrt(sum(x**2) / right1 * 35)
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return left, right
