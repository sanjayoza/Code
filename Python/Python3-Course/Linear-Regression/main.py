from csv import reader
from math import sqrt
from random import seed
from linear import evaluate_algorithm
from linear import simple_linear_regression

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


# run the regression
def run_test():
	seed(1)
	filename = input("Enter csv file name > ")
	delim = input("Enter delimiter > ")
	dataset = load_csv(filename, delim)
	# print(dataset)
	# print("len of dataset[0] {}" .format(len(dataset[0])))
	for i in range(len(dataset[0])):
		str_column_to_float(dataset, i)

	split = 0.6
	rmse = evaluate_algorithm(dataset, simple_linear_regression, split)
	print("RSME: {}" .format(rmse))


if __name__ == "__main__":
	run_test()