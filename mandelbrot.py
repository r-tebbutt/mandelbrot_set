import numpy as np
from PIL import Image
import cmath
import time 


height = 1000
width = 1000

data = np.zeros( (height, width,3), dtype=np.uint8 )

re_lb = -2
re_ub = 2
im_lb = -2
im_ub = 2

re_interval = (re_ub - re_lb) / width
im_interval = (im_ub - im_lb) / height


def test_converge(re, im):
    z = complex(re, im)
    seed = complex(0,0)
    iterations = 0
    
    while seed.real**2+seed.imag**2 < 10 and iterations < 100:
            new_z = seed*seed + z
            seed = new_z
            iterations += 1

    if iterations == 100:
        return 0
    else:
        return (iterations * 3.6)

start = time.time()

for i in range(width):
    re_val = re_lb + i * re_interval
    for j in range(height):
        im_val = im_lb + j * im_interval

        colour = test_converge(re_val, im_val)
        if colour == 0:
            data[j, i] = (0,0,0)
        else:
            data[j,i] = (215, 254, colour) # makes a nice fade out as divergence speed increases - as you go away from the fractal




mandelbrot_set = Image.fromarray(data, mode = "HSV")
mandelbrot_set.show()
end = time.time()
print(end - start)






