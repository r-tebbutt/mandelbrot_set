#define STB_IMAGE_WRITE_IMPLEMENTATION
#include <iostream>
#include <cstdlib>
#include <complex>
#include <cmath>
#include "stb_image_write.h"
#include <chrono>

using namespace std;

unsigned char test_converge(double, double);

const int height = 1080, width = 1920;
unsigned char pixel_array[height * width * 3];

int main() {

	double re_ub, re_lb, im_ub, im_lb, re_interval, im_interval, re_val, im_val;
	unsigned char colour;
	

	re_ub = 2 * width / height;
	re_lb = -2 * width / height;
	im_ub = 2;
	im_lb = -2;

	re_interval = (re_ub - re_lb) / width;
	im_interval = (im_ub - im_lb) / height;

	cout << "Generating Image..." << endl;

	auto start = chrono::high_resolution_clock::now();

	for (int i = 0; i < height; i++) {
		im_val = im_lb + i * im_interval;

		for (int j = 0; j < width; j++) {
			re_val = re_lb + j * re_interval;

			colour = test_converge(re_val, im_val);
			
			pixel_array[(i * width + j) * 3] = colour * 2;
			pixel_array[(i * width + j) * 3 + 1] = 0;
			pixel_array[(i * width + j) * 3 + 2] = colour * 2;
	
		}
		
	}

	char const* filename = "mandelbrot.jpg";
	stbi_write_jpg(filename, width, height, 3, &pixel_array[0], 100);
	
	auto stop = chrono::high_resolution_clock::now();
	auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
	
	cout << "Time to generate image: " << endl;
	cout << duration.count() << " microseconds" << endl;
}



unsigned char test_converge(double re, double im) {

	complex<double> z(re, im), seed(0, 0);
	unsigned char iterations = 0;

	while ((pow(real(seed), 2) + pow(imag(seed), 2) < 3) && iterations < 100) {
		seed = pow(seed, 2) + z;
		iterations++;
	}

	if (iterations == 100) {
		return 0;
	}
	else {
		return iterations;
	}
	

}