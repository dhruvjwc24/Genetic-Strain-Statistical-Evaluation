import math

def mean(data):
    count = 0
    numElems = len(data)
    for val in data:
        count+=val
    avg = count/numElems
    return avg

def stdDev(data):
    count = 0
    avg = mean(data)
    numElems = len(data)
    for val in data:
        count+= (val-avg)**2
    count/=numElems
    count = math.sqrt(count)
    return count

def get_values(data):
    avg = mean(data)
    sD = stdDev(data)
    numElems = len(data)
    return avg, sD, numElems

def main():
    myList = [5.99342831, 4.7234714 , 6.29537708, 8.04605971, 4.53169325,  4.53172609, 8.15842563, 6.53486946, 4.06105123, 6.08512009]
    avg, standardDev, numElements = get_values(myList)
    print("\n\tMean: {}\n\tStandard Deviation: {}\n\tNumber of Elements: {}\n".format(avg, standardDev, numElements))

if __name__ == "__main__": main()