import numpy as np
import time
import sys

LOWEST_NUMBER = -100
HIGHEST_NUMBER = 100
ARRAY1_SIZE = 500
ARRAY2_SIZE = 1000

np.random.seed(1063199)

arr1 = np.random.randint(LOWEST_NUMBER,HIGHEST_NUMBER,ARRAY1_SIZE)
arr2 = np.random.randint(LOWEST_NUMBER,HIGHEST_NUMBER,ARRAY2_SIZE)

def printformattedData(time, max, start, end):
    print("Time: " + str(time)+ "  \tMax: " + str(max) + "\tStart: " + str(start) + "\tEnd: "+ str(end) + "\n")

def maxSubOrderN3(arr):
    maxSum = 0
    for j in range(len(arr)):
        for k in range(j, len(arr)):
            sum = 0
            for i in range(j,k+1):
                sum += arr[i]
            
            if sum > maxSum:
                maxSum = sum
                start = j
                end = k

    return maxSum, start, end



def maxSubOrderN2WithHelpingArray(arr):
    sumsArray = [0] * len(arr)
    sumsArray[0] = arr[0]

    for i in range(1, len(arr)):
        sumsArray[i] = sumsArray[i-1] + arr[i]

    maxSum = 0
    for j in range(len(arr)):
        for k in range(j, len(arr)):
            sum = sumsArray[k] - sumsArray[j]

            if sum>maxSum:
                maxSum = sum
                start = j + 1
                end = k

    return maxSum, start, end



def maxSubOrderN2WithoutHelpingArray(arr):
    maxSum = 0
    for j in range(len(arr)):
        sum = 0
        for k in range(j, len(arr)):
            sum += arr[k]

            if sum>maxSum:
                maxSum = sum
                start = j
                end = k

    return maxSum, start, end



def maxSubOrderN(arr):
    maxSum = max(0, arr[0])
    prevMaxSum = 0
    start = 0

    for i in range(len(arr)):
        curMaxSum = max(0, prevMaxSum+arr[i])

        if curMaxSum > maxSum:
            end = i
            maxSum = curMaxSum

        prevMaxSum = curMaxSum

    sum = maxSum
    for i in range(end, 0, -1):
        sum -= arr[i]

        if sum <= 0:
            start = i
            break

    return maxSum, start, end



def max_crossing_subarray(arr, low, mid, high):
    left_sum = -sys.maxsize
    current_sum = 0
    for i in range(mid, low-1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    right_sum = -sys.maxsize
    current_sum = 0
    for j in range(mid+1, high+1):
        current_sum += arr[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return (left_sum+right_sum, max_left, max_right)


def maxSubOrderNLogn(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    else:
        mid = (low+high)//2
        left_sum, left_low, left_high = maxSubOrderNLogn(arr, low, mid)
        right_sum, right_low, right_high = maxSubOrderNLogn(arr, mid+1, high)
        cross_sum, cross_low, cross_high = max_crossing_subarray(
            arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_sum, left_low, left_high)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return ( right_sum, right_low, right_high)
        else:
            return (cross_sum, cross_low, cross_high)



#Time for O(n^3)
print("O(n^3)")
print("Array with " + str(len(arr1)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN3(arr1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("Array with " + str(len(arr2)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN3(arr2)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("----------------------------------------------")

#Time for O(n^2) with helping array
print("O(n^2) with helping array")
print("Array with " + str(len(arr1)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN2WithHelpingArray(arr1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("Array with " + str(len(arr2)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN2WithHelpingArray(arr2)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("----------------------------------------------")

#Time for O(n^2) without helping array
print("O(n^2) without helping array")
print("Array with " + str(len(arr1)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN2WithoutHelpingArray(arr1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("Array with " + str(len(arr2)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN2WithoutHelpingArray(arr2)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("----------------------------------------------")


#Time for O(n*logn)
print("O(n*logn)")
print("Array with " + str(len(arr1)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderNLogn(arr1, 0, len(arr1)-1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("Array with " + str(len(arr2)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderNLogn(arr2, 0, len(arr2)-1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("----------------------------------------------")

#Time for O(n)
print("O(n)")
print("Array with " + str(len(arr1)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN(arr1)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)

print("Array with " + str(len(arr2)) + " elements")
startTime = time.time()
a,b,c = maxSubOrderN(arr2)
endTime = time.time()
totalTime = endTime -startTime
printformattedData(totalTime,a,b,c)