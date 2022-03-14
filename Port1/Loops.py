#Choose a number and multiply it
def IterationFunction(i, value):
    value +=1
    value *=1
    return value


#print out value 10 times
CurrentValue = 0

for iteration in range(0,10):

    CurrentValue = IterationFunction(iteration,CurrentValue)

    print(CurrentValue)

    print("Current Value: {0}".format(CurrentValue))

