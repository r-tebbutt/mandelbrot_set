# mandelbrot_set
 

mandelbrot.py:

This program generates an image of the mandelbrot set. The size in pixels of the image and the range and domain to be viewed can be changed.

The mandelbrot set contains complex numbers z for which recursing f(c) = c^2 + z diverges to infinity with an inital/seed value of c = 0.


multiprocess.py:

After the initial code was completed (see mandelbrot.py), an optimised version (see multiprocessing.py), which incorporates multiprocessing for 
a 6 core CPU, was written and seen to decrease processing time from ~15 seconds to ~10 seconds for a 1000 x 1000 image on my computer, a 33% decrease.

The reason this is far from a 6 - fold decrease is because I could not find a way to split the manual pixel assigning between the 6 cores,
as each core can only make a change to something if it is in shared memory, i.e. there is a lot of overhead in the program. There very well may be a faster way to do this.

I was unable to use Image.fromarray() to generate an image in multiprocess.py. I'm not sure why it didn't work but it created very incorrect images
while Image.putpixel() was working just fine. Assigning pixels manually is much slower than using Image.fromarray.

bifurcations.py:

This program generates the classic bifurcation diagram from mandelbrot numbers. 
This is done by moving across the real axis, and assigning a value to each number equal to the value that the number converges to when 
recursed into the mandelbrot formula. The plot is this convergence value against the actual number. Some numbers converge to multiple values and cycle through them periodically,
this causes the forks or bifurcations.
It is interesting that this ubiquitous plot crops up again in the mandelbrot set.
From the plot, the Feigenbaum constant can be seen to be about 4.3, using the first and second bifurcation.

julia.py:

This program generates images of julia sets, which are fractals of a similar concept to the mandelbrot set, though use a slightly different recursion formula.
The seed begins as the complex number in question, and the set contains complex numbers where f(z) = z^2 + c does not diverge to infinity on recursion - in this
case, c is a constant complex number, and z is the complex number being tested.

The fractals generated can be drastically changed by subtly altering the recursion equation - playing around with this is the fun part.

mandelbrot.cpp:

This program is a replica of mandelbrot.py, but written in c++. This creates the same image in 4 seconds with no compiler optimisation, and 2.7 seconds with /02 optimisation (which favours speed), emphasising how much faster c++ runs compared to python.

This was a lesson in utilising multiple cores to improve performance and let me experience the drastic difference in execution speeds of compiled vs interpreted languages.
I learnt more about fractals, and I got a very pretty desktop background for my efforts.



