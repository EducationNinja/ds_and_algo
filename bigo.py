# O(a) -> O(n)
def example_1(a_list):
	for a in a_list:
		print(a)


# O(a * a) -> O(a^2) -> O(n^2)
def example_2(a_list):
	for x in a_list:
		for y in a_list:
			print(x, y)


# O(a + a) -> O(2a) -> O(a) -> O(n)
def example_3(a_list):
	# O(a)
	for x in a_list:
		print(x)

	# O(a)
	for y in a_list:
		print(y)

# O(a) + O(b) -> O(a + b)
def example_4(a_list, b_list):
	# O(a)
	for x in a_list:
		print(x)

	# O(b)
	for y in b_list:
		print(y)

# O(n) + (n^2) -> O(n^2)
def example_5(a_list):
	# O(n)
	for a in a_list:
		print(a)

	# O(n^2)
	for x in a_list:
		for y in a_list:
			print(x, y)

# O(a) * O(b) -> O(a * b)
def example_6(a_list, b_list):
	for x in a_list:
		for y in b_list:
			print(x, y)


# O(a^3) + O(b)
def example_5(a_list, b_list):
	# O(b)
	for a in b_list:
		print(a)

	# O(a^2)
	for x in a_list:
		for y in a_list:
			print(x, y)

	# O(a^3)
	for x in a_list:
		for y in a_list:
			for z in a_list:
				print(x,y,z)