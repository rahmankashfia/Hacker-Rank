f = open("command.txt")
count = int(f.readline())
ls = []
while count > 0:
	temp = f.readline().split()

	if temp[0] == "print":
		print(ls)
	elif temp[0] == "insert":
		ls.insert(int(temp[1]), int(temp[2]))
	elif temp[0] == "remove":
		ls.remove(int(temp[1]))
	elif temp[0] == "reverse":
		ls.reverse()
	elif temp[0] == "pop":
		ls.pop()
	elif temp[0] == "sort":
		ls.sort()
	elif temp[0] == "append":
		ls.append(int(temp[1]))
	else:
		print("uc")
	count -= 1

f.close()