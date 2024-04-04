n = input()

dc = {}
l =0
for x in n:
    if x in dc and x.isalpha():
        dc[x] += 1
    elif x not in dc and x.isalpha():
        dc[x] = 1
for x in range(97,123):
    if chr(x) in dc:
        print(chr(x),dc[chr(x)])
    else:
        print(chr(x),l)
for x in range(65,91):
    if chr(x) in dc:
        print(chr(x),dc[chr(x)])
    else:
        print(chr(x),l)