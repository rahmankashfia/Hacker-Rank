import numpy

a = numpy.array([[1, 2, 3],
				 [4, 5, 6],
				 [7, 8, 9],
				 [10, 11, 12]])

print(numpy.min(a))
print(numpy.min(a, axis = 0))
print(numpy.min(a, axis = 1))


s1 = "4 2"
s2 = ["2 5", "3 7", "1 3", "4 0"]

dim = list(map(int, s1.split()))
row = dim[0]
col = dim[1]

a = []
for x in s2:
	temp = list(map(int, x.split()))
	a.append(temp)

print(max(numpy.min(a, axis = 1)))
