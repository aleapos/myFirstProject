num = '453857'
numbers = list(num)
dif = []
print(numbers)
x = 0
for i in range(len(numbers)):
    if i-1 in range(len(numbers)):
        x = int(numbers[i]) - int(numbers[i - 1])
        dif.append(x)

print(dif)
position = (dif.index(max(dif)))
print(numbers[position],numbers[position + 1])
