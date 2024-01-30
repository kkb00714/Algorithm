s = input()

for x in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(x, 'i')
print(len(s))
