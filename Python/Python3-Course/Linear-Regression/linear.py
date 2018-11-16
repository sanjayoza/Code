# example from https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/

from csv import reader
from math import sqrt
from random import randrange

# calculate the mean of valules
def mean(values):
	return sum(values) / float(len(values))

# calculate variance - is a sum squared difference for
# each value from the mean value
def variance(values, mean):
	return sum([(x - mean) ** 2 for x in values])

# calculate co-variance - co-variance of 2 groups of numbers
# describes how those numbers change together.
# Covariance is a generalization of correlation. Correlation
# describes the relationship between two group of numbers,
# where as covariance can describe the relationship between two
# or more groups of numbers. Covariance can be normalized to
# produce a correlation value.
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

# estimate two coefficients
# b1 = sum((x(i) - mean(x)) * (y{i) - mean(y)))) / sum(x(i) - mean(x))^2
# b1 = covariance(x, y) / variance(x)
# b0 = mean(y) - b1 * mean(x)
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean = mean(x)
	y_mean = mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]


# once the coefficients are calculated we can use them to make predicitions
# simple linear regression is a line defined by coefficients on the 
# training data. The equation is:
# y = b0 + b1 * x
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions


# split a dataset into a train and test set
def train_test_split(dataset, split):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

# evaluate alogrithm, to evalate the predicitons
def evaluate_algorithm(dataset, algorithm, split, *args):
	train, test = train_test_split(dataset, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	# print("train: {}" .format(train))
	# print("test_set: {}" .format(test_set))
	predicted = algorithm(train, test_set, *args)
	# print(predicted)
	actual = [row[-1] for row in test]
	rmse = rmse_metric(actual, predicted)
	return rmse

# Calculate root mean squared error of the predictions
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
	return sqrt(mean_error)



if __name__ == "__main__":
	print("Entered main")

	dataset = [[1,1], [2,3], [4,3], [3,2], [5,5]]
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	print("x is {}" .format(x))
	print("y is {}" .format(y))
	mean_x, mean_y = mean(x), mean(y)
	var_x, var_y = variance(x, mean_x), variance(y, mean_y)
	print("x stats: mean = {:0.3f} variance = {:7.3f}" .format(mean_x, var_x))
	print("y stats: mean = {:0.3f} variance = {:7.3f}" .format(mean_y, var_y))

	covar = covariance(x, mean_x, y, mean_y)
	print("Covariance {:0.3f}" .format(covar))

	b0, b1 = coefficients(dataset)
	print("Coefficients b0: {:0.3f}  b1: {:0.3f}" .format(b0, b1))

	rmse = evaluate_algorigthm(dataset, simple_linear_regression)
	print("RMSE: {:0.3f}" .format(rmse))