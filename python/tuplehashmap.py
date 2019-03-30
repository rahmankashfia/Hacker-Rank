n = 5
_input = "1 2 3 4 5 "

int_ls = map(int, _input.split())


t = tuple(int_ls)
print(hash(t))