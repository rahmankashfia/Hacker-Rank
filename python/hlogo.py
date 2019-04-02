n = 5
i = 4
for x in range(0,n):
	print("H".ljust(2*x+1, "H").rjust(i+2*x+1, " "))
	i = i - 1
	
for x in range(0,n+1):
	print("H".rjust(3, " ").ljust(7, "H").ljust(19, " ").ljust(24, "H"))

for x in range(0,3):
	print("H".rjust(25, "H").rjust(27, " "))

for x in range(0,n+1):
	print("H".rjust(3, " ").ljust(7, "H").ljust(19, " ").ljust(24, 	"H"))

for x in range(0,n):
	print("H".ljust(2*n-1-(2*x), "H").rjust(27 - (x+1), " "))
	