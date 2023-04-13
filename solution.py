import pandas as pd
import numpy as np


chat_id = 441809625 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.03
    delta = y.mean() - x.mean()
    
    pvalue = ttest_ind(x, y, equal_var=False).pvalue
    
    if (pvalue < 2 * alpha and delta < 0):
        buf = True
    else: 
        buf = False
        
    return buf
