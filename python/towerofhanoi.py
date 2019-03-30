def toh(s, d, e, n):

	if n <= 0:
		print("return from toh({}, {}, {}, {})".format(s, d, e, n))
		return
	#print("calling toh({}, {}, {}, {} -1)".format(s, e, d, n))
	toh(s, e, d, n-1)
	#print("after toh({}, {}, {}, {})".format(s, d, e, n))
	print("move {} to {} disc {}".format(s, d, n))
	#print("calling toh({}, {}, {}, {} -1)".format(e, d, s, n))
	toh(e, d, s, n-1)


toh("s", "d", "e", 3)