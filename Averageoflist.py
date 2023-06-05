l = list(map(int, input("Enter the numbers: ").split()))

count = 0
sum = 0
for i in range(len(l)):
    count = count + 1
    sum = sum + l[i]
average = sum/count
print("Count {}, Sum {}, Average {}".format(count, sum, average))