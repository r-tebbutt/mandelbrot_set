import numpy as np
from PIL import Image
import cmath
import time
from multiprocessing import Process, Manager

width = 1000
height = 1000

re_lb = -2 * (width / height) # factor at end ensures it doesn't look stretched
re_ub = 2 * (width / height)
im_lb = -2
im_ub = 2

re_interval = (re_ub - re_lb) / width
im_interval = (im_ub - im_lb) / height

img = Image.new( 'RGB', (width, height), "black")

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




def generate_mandelbrot(start_row, end_row, pixels):
    
    for i in range(start_row, end_row):
        
        temp_list = []
        im_val = im_lb + i * im_interval
        
        for j in range(width):
            
            re_val = re_lb + j * re_interval
            colour = int(test_converge(re_val, im_val))
            temp_list.append((colour, 0, colour))

        pixels[i] = temp_list
        

if __name__ == '__main__':
    
    manager = Manager() 
    pixels = manager.list(range(height)) # creates shared memory list - can be accessed and changed by all cores
    
    divs = [int(i * height / 6) for i in range(7)] # calculates divisions for each core to process

    my_thread0 = Process(target=generate_mandelbrot, args=(divs[0], divs[1], pixels))
    my_thread1 = Process(target=generate_mandelbrot, args=(divs[1], divs[2], pixels))
    my_thread2 = Process(target=generate_mandelbrot, args=(divs[2], divs[3], pixels))
    my_thread3 = Process(target=generate_mandelbrot, args=(divs[3], divs[4], pixels))
    my_thread4 = Process(target=generate_mandelbrot, args=(divs[4], divs[5], pixels))
    my_thread5 = Process(target=generate_mandelbrot, args=(divs[5], divs[6], pixels)) # this is for a 6 core CPU


    start = time.time()

    my_thread0.start() # starts all the multicore processing
    my_thread1.start()
    my_thread2.start()
    my_thread3.start()
    my_thread4.start()
    my_thread5.start()
    my_thread0.join() # .join waits for all the cores to finish before proceeding with the program
    my_thread1.join()
    my_thread2.join()
    my_thread3.join()
    my_thread4.join()
    my_thread5.join()
    
   
    pixels_list = list(pixels) # manager.list is a listproxy which didn't work with .putpixel
    
    
    for i in range(height):

        for j in range(width):

            img.putpixel((j, i), (pixels_list[i][j]))
    
    img.show()
    img.save('mandelbrot.png')
    end = time.time()
    print(end - start)
   

