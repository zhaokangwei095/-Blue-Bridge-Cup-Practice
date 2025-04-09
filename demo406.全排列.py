import sys
 
for line in sys.stdin:
    a = line.split()

def sort_f(a, s):
    if len(a) == 1:
        print(f'{s} {a[0]}')
        return

    a.sort()
    for n in a:
        b = a.copy()
        b.remove(n)
        if len(s) > 0:
            s_t = s + ' ' + str(n)
        else:
            s_t = str(n)
        sort_f(b, s_t)


ns = [x for x in range(1, 9)]
sort_f(ns, '')