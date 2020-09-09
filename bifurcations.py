import numpy as np
from PIL import Image
import cmath
import time
from multiprocessing import Process, Manager
import matplotlib.pyplot as plt


width = 1000
height = 1000

re_lb = -2 * (width / height) # factor at end ensures it doesn't look stretched
re_ub = 2 * (width / height)
im_lb = -2
im_ub = 2

re_interval = (re_ub - re_lb) / width
im_interval = (im_ub - im_lb) / height

re_values = []
final_values = []


def test_converge(re, im):
    z = complex(re, im)
    seed = complex(0,0)
    iterations = 0
    branch_values = []
    while seed.real**2+seed.imag**2 < 10 and iterations < 100:
            new_z = seed*seed + z
            seed = new_z
            iterations += 1
    branch_values.append(seed.real)
    
    if iterations == 100:
        seed_copy = seed
        for i in range(15):
            next_seed = seed_copy* seed_copy + z
            seed_copy = next_seed
            if seed_copy.real not in branch_values:
                branch_values.append(seed_copy.real)
        
        final_values.append(branch_values)
    



        
for i in range(-3000, 300, 1):
    re_values.append(i/1000)
    test_converge(i/1000, 0)


fig, ax = plt.subplots()

for x, y in zip(re_values, final_values):
    
    ax.scatter([x] * len(y), y, s = 0.01)

plt.show()    
    





   

