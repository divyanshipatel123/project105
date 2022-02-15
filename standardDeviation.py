import csv 
import math
# function to get the mean
def mean(data):
    n = len(data) 
    total = 0
    for i in data:
        total += int(i)
    mean = total/n
    return mean
#function to get the standard deviation
def StandardDeviation(dataset):
    #open and read csv
    with open (str(dataset) , newline = "") as f:
        reader = csv.reader(f)
        fileData = list(reader)
    # filter and keep the main data
    data = fileData[0]
    #calling mean function ti get the mean
    mean_ = mean(data)
    squaredList = []
    # for loop to get the difference 
    for i in data:
        a = int(i) - mean_
        a = a**2
        squaredList.append(a)
    sum = 0
    # for loop to sum up all the squares
    for i in squaredList:
        sum += i 
    #dividing the sum by (number of values - 1)
    result  = sum / (len(data) - 1)
    # taking the square root of the result to the the final deviation
    Standard_Deviation = math.sqrt(result)
    print("The standard deviation of the given dataset is : ",Standard_Deviation)

#give the file name in double inverted commas
StandardDeviation("data.csv")