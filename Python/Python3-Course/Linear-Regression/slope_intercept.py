# in youtube look for sentdex for machine learning videos p10 - p12
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
#style.use('fivethirytyeight')

#xs = np.array([1,2,3,4,5,6], dtype=np.float64)
#ys = np.array([5,4,6,5,6,7], dtype=np.float64)


# hm - how many
def create_dataset(hm, variance, step=2, correlation=False):
	val = 1
	ys = []
	for i in range(hm):
		y = val + random.randrange(-variance, variance)
		ys.append(y)
		if correlation and correlation == 'pos':
			val += step
		elif correlation and correlation == 'neg':
			val -= step
	xs = [i for i in range(len(ys))]
	return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
	m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
		  ((mean(xs) * mean(xs)) - mean(xs*xs)))

	b = mean(ys) - m*mean(xs)
	return m, b

def squared_error(ys_orig, ys_line):
	return sum((ys_line - ys_orig) ** 2)

def coefficient_of_determination(ys_orig, ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	square_error_regr = squared_error(ys_orig, ys_line)
	square_error_y_mean = squared_error(ys_orig, y_mean_line)

	return 1 - (square_error_regr / square_error_y_mean)


if __name__ == "__main__":

	nitems = int(input("Enter number of items > "))
	variance = int(input("Enter variance > "))
	nstep = int(input("Enter step > "))
	corr = input("Enter correlation pos, neg, False, True > ")
	xs, ys = create_dataset(nitems, variance, nstep, corr)
	#xs, ys = create_dataset(40, 30, 2, 'pos')
	print("x: \n{}" .format(xs))
	print("y: \n{}" .format(ys))
	m, b = best_fit_slope_and_intercept(xs, ys)

	print("slope {} y-intercept {}" .format(m, b))

	regression_line = [(m*x) + b for x in xs]
	#print("Regression line {}" .format(regression_line))

	predict_x = 8
	predict_y = (m*predict_x) + b

	print("predict_x {} predict_y {}" .format(predict_x, predict_y))

	r_squared = coefficient_of_determination(ys, regression_line)

	print(r_squared)

	plt.scatter(xs,ys)
	plt.scatter(predict_x, predict_y, s=100, color='r')
	plt.plot(xs, regression_line)
	plt.title("Linear Regression")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()