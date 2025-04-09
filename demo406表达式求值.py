a=eval(input())
if a>9999:
    b=str(a)
    c=b[-4:]
    print(int(c))
else:
    print(a)




'''sum=0
for i in input().split('+'):
    sum+=eval(i)
print(sum%10000)
'''