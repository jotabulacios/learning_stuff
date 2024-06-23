# Create FFT from zero
import numpy as np
from math import pi, exp

def FFT(x):
    N = len(x)
    if N <= 1:
        return x
    even = FFT(x[0::2])
    odd = FFT(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]

