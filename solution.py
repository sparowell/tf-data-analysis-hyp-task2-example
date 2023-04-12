import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    #ks_2samp
    #p = cramervonmises_2samp(x, y).pvalue # Это как раз CVM
    p = MMD(compute_kernel="rbf", gamma=10).test(x, y)[1]
    return p <= 0.01 
