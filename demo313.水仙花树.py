num=int(input('请输入一个三位数:'))

if num==pow(num//100,3)+pow(num%10,3)+pow(num//10%10,3):
    print("yes")
else:
    print("no")