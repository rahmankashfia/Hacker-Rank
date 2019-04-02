s = "123"
aln = False
al = False
dig = False
low = False
up = False
for x in range(len(s)):
    if s[x].isalpha() and al == False:
        al = True
    if s[x].isdigit() and dig == False:
        dig = True
    if al == True and dig == True: #number or alphabet
        aln = True
    if s[x].islower() or low == False: 
        low = True
    if s[x].isupper() and up == False:
        up = True
print(aln)
print(al)
print(dig)
print(low)
print(up)