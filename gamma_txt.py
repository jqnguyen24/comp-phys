import math
import pdb





def gamma_if_int(t):
    return math.factorial(t-1)

def f(x, t):
	return (x**(t-1))*(math.exp(-x))

def fractionaldifference(prev, curr):       
	frac_diff = (curr - prev)/float(curr)
	return frac_diff

def gamma_otherwise(t, tol):  
	#pdb.set_trace()
	initial = 0
	final = 1000
	frac_diff = 1.
	dx = 1.
	integral_previous = 0.
	steps = (final - initial)/dx
	while frac_diff > tol:
		integral_current = 0.
		for j in range(0, int(steps) + 1):
			height = f(initial + j*dx, t)
			area = dx*height
			integral_current += area
		frac_diff = abs(fractionaldifference(integral_previous, integral_current))
		integral_previous = integral_current
		steps *= 2.
		dx /= 2.
	return integral_previous, frac_diff
	
def computegamma(t, tolerance):
	"""
Program takes user input from terminal, the value of t and tolerance desired, and determines how to calculate the
gamma function.  If the value of t is an integer, evaluate the gamma function with gamma_if_int(t).
If the value of t is a float, evaluate the gamma function with gamma_otherwise(t, tol).  If evaluating the integral way,
take the desired tolerance to get the value of dx small enough so the tolerance is met.  If the value of t is above 100
or below 1, the program will return an message saying to choose a value between 1 and 100, inclusive.

	>>> computegamma(1, 1e-4) == 1
	True
	
	"""
	if t < 1. or t > 100.:
		return "Please enter value that is between 1 and 100, inclusive."
	str_t = str(t)
	if str_t[len(str_t)-1] == '0':
		int_t = int(t)
		return gamma_if_int(int_t)
	else:
		return gamma_otherwise(t, tolerance)


if __name__ == "__main__":

	import doctest
	import argparse
	from math import log, log1p



	parser = argparse.ArgumentParser()
	parser.add_argument('-x',	type = float)
	parser.add_argument('-y', type = float)
	args = parser.parse_args()
	x = args.x
	y = args.y
	estimated_answer = computegamma(x, y)
	print estimated_answer