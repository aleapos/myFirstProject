num = [12, 3, 1, -5, -4, 7]
m=0
for i in range(0,len(num) - 2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            if num[i] + num[j] + num[k] == num[0]:
                m = m+1

if m>0:
    print(True)
else:
    print(False)




