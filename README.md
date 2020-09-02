# mandelbrot_set
 
This program generates an image of the mandelbrot set. The size in pixels of the image and the range and domain to be viewed can be changed.

The mandelbrot set contains complex numbers z for which recursing f(c) = c^2 + z diverges to infinity with an inital/seed value of c = 0.

After the initial code was completed (see mandelbrot.py), an optimised version (see multiprocessing.py), which incorporates multiprocessing for 
a 6 core CPU, was written and seen to decrease processing time from ~15 seconds to ~10 seconds for a 1000 x 1000 image on my computer, a 33% decrease.

The reason this is far from a 6 - fold decrease is because I could not find a way to split the manual pixel assigning between the 6 cores,
as each core can only make a change to something if it is in shared memory, i.e. there is a lot of overhead in the program. There very well may be a faster way to do this.

I was unable to use Image.fromarray() to generate an image in multiprocess.py. I'm not sure why it didn't work but it created very incorrect images
while Image.putpixel() was working just fine. Assigning pixels manually is much slower than using Image.fromarray.


Anyway, this was a lesson in utilising multiple cores to improve performance and I got a very pretty desktop background for my efforts.

