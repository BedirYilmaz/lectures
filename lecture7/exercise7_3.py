import math

def estimate_pi():
    
    res = 0
    k = 0
    while True:

        step_res = math.factorial(4*k) * (1103 + k * 26390) / \
                   (math.factorial(k)**4 * 396**(4*k))
        
        if step_res < 1e-15:
            break
        
        res += step_res
        k += 1

    
    coeff = 2*math.sqrt(2)/9801
    
    return res * coeff

estimated_pi = estimate_pi()

print(math.pi - estimated_pi**-1)