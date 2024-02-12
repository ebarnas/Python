#This will count out all of the beer stanza, it will go on for 99 lines
count = 99
while count > 1:
    print(str(count) + " bottles of beer on the wall")
    print(str(count) + " bottles of beer")
    print("take one down, pass it around")
    print(str(count - 1) + " bottles of beer on the wall")
    count = count - 1
    if count == 1:
        print(str(count) + " bottle of beer on the wall")
        print(str(count) + " bottle of beer")
        print("take one down, pass it around")
        print("No bottles of beer on the wall!")