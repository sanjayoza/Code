def towers_of_hanoi(numdisks, startpeg = 1, endpeg = 3):
	if numdisks:
		towers_of_hanoi(numdisks - 1, startpeg, 6 - startpeg - endpeg)
		print("move disk {} from peg {} to peg {}" .format(numdisks, startpeg, endpeg))
		towers_of_hanoi(numdisks - 1, 6 - startpeg - endpeg, endpeg)


towers_of_hanoi(4)