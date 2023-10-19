myData = {
    "effective top tube length": 515, 
    "seat tube length": 500, 
    "seat tube angle": 74.4, 
    "head tube angle": 70.5, 
    "stack": 513, 
    "reach": 367, 
    "standover height": 755
} 

myKeys = []
myValues = []
# parrallel iterations: working with k & v at the same time
for k, v in myData.items():
    print("key:" + str(k) + "' value: " + str(v))
    myKeys.append(k) #append() method will ADD things to the LIST (array)
    myValues.append(v)

print("ALL KEYS: " + str(myKeys))
print("ALL Values: " + str(myValues))



