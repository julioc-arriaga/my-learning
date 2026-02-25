#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    elementCount = 0
    if responseTimes is not None and len(responseTimes) > 0:
        for i in range(1, len(responseTimes)):
            prevAvg = sum(responseTimes[:i]) / i
            if responseTimes[i] > prevAvg:
                elementCount += 1
        return elementCount
    else:
        return 0
    

inputArray = [100, 200, 150, 300]
print("Output: ",countResponseTimeRegressions(inputArray))


