import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p = ks_2samp(x, y, alternative="two-sided").pvalue
    return p < 0.01 # Ваш ответ, True или False
