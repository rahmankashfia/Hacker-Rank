import string

s = "HackerRank.com presents \"Pythonist 2\"."
r = []
for x in range(len(s)):
		if s[x] in string.ascii_lowercase or s[x] in string.ascii_uppercase:
			if s[x].isupper():
				r.append(s[x].lower())
			elif s[x].islower():
				r.append(s[x].upper()) 
		else:
			r.append(s[x])
print(''.join(r))