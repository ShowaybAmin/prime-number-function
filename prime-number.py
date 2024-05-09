a = []

b = int(input("Last number to search for prime number: "))

def _solution_():

	flag = True

	for i in range(2, p):

		if (p % i) == 0:

			flag = False

			break

	if flag:

		a.append(p)

if b < 2:

	print("Sorry...The first prime number is 2")

else:

	for p in range(2, b+1):

		_solution_()

print(a)

