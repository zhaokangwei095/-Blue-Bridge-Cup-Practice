a[0]=[0,0,0]
a[1]=[1,2,3]
a[2]=[4,5,6]
a[3]=[7,8,9]
while not (mima=input())==None:
    def chongfu(mima):
        if len(set(mima)) == len(mima):
        print("NO")
        return False
        else:
            return True
    def find_2d_index(lst, value,value_next):
        for i, row in enumerate(lst):         # i 表示行号，row 是每一行
            if value in row:                  # 如果这个值在当前行
                j = row.index(value)
        for m, row in enumerate(lst):         # i 表示行号，row 是每一行
            if value in row:                  # 如果这个值在当前行
                n = row.index(value_next)
            if i+1!=m or  i-1!=m or j+1!=n or j-1!=n:
               print("NO")
                
                         







