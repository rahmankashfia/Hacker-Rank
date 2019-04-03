s = ")))((("
t = []
matched = True

for x in s:
	if x == "(":
		t.append(x)
	if x == ")":
		if len(t) == 0:
			matched = False
		else:
			t.pop()

if len(t) > 0:
	matched = False
print(matched)

		
