# in youtube look for sentdex for machine learning videos p10 - p12
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
from csv import reader

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

# Read the dataset from csv file
def load_csv(filename, delim):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file, delimiter=delim)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# convert string columns to float
def str_column_to_float(dataset, column):
	for row in dataset:
		# print("row is {}" .format(row))
		row[column] = float(row[column].strip())


if __name__ == "__main__":

	filename = input("Enter csv file name > ")
	delim = input("Enter delimiter > ")
	dataset = load_csv(filename, delim)
	for i in range(len(dataset[0])):
		str_column_to_float(dataset, i)

	xs = list()
	ys = list()

	for x in range(len(dataset)):
		xs.append(dataset[x][0])
		ys.append(dataset[x][1])
	

	xs = np.array(xs, dtype=np.float64)
	ys = np.array(ys, dtype=np.float64)
	
	print("x: \n{}" .format(xs))
	print("y: \n{}" .format(ys))
	m, b = best_fit_slope_and_intercept(xs, ys)

	print("slope {} y-intercept {}" .format(m, b))

	regression_line = [(m*x) + b for x in xs]
	#print("Regression line {}" .format(regression_line))

	predict_x = 20
	predict_y = (m*predict_x) + b

	print("predict_x {} predict_y {}" .format(predict_x, predict_y))

	r_squared = coefficient_of_determination(ys, regression_line)

	print("r squared {}" .format(r_squared))

	plt.scatter(xs,ys)
	plt.scatter(predict_x, predict_y, s=100, color='r')
	plt.plot(xs, regression_line)
	plt.title("Linear Regression")
	plt.xlabel("X")
	plt.ylabel("Y")
	plt.show()