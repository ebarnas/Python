#This will run if the numbers between 1-300 are divisible by 7
for count in range(1, 300):
    if count % 7:
        continue
    print(count)