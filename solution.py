import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = cramervonmises_2samp(x, y).pvalue # Это как раз CVM
    return p <= 0.01 
