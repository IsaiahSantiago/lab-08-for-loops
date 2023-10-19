highestnum = 0
# initiate highestnum variable as 0
# we will replace this 0 inside our for loop...

for i in range(0, 4, 1):
    userinput = input("Number please...")
    userInt = int(userinput)
    print("user inputed; " + str(userinput))
    if userInt > highestnum:
        highestnum = userInt
    else:
        print ("This is not the highest number!")
print("The highest number entered is:" + str(highestnum))
