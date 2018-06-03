import math

#INTERMEDIATE STATISTICS

number_of_laptops = [30, 40, 50, 60, 311, 23, 13]

#Central tendencies

print("\nMedian = ")

#Mean : defining how to calculate mean
def mean(x) :
    return sum(x) / len(x)
print(mean(number_of_laptops)) #printing mean of number of laptops

#Median : doesn't depend on all data values
print("\nMedian = ")
def median(input):
    n = len(input) #determining length of input
    sorted_v = sorted(input) #sorting the inputted list
    midpoint = n // 2 #calculating the midpoint index
    if n % 2 == 1:  #if odd number of elements
        return sorted_v[midpoint]
    else:   #if even number of elements
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi])/2 #avg. of element before middle one and current median
print(median(number_of_laptops))


#Dispersion :
#Dispersion measures how far apart, or how spread apart data is
#Near 0 = not as spread out
#Larger Values = more spread out
print()
print("Range = ")
def range(input):
    return max(input) - min(input)
print(range(number_of_laptops))


#Variance : measure of dispersion
print()
print("Variance = ")
def sum_of_squares(input):
    sum = 0
    for i in input:
        sum += i * i;
    return sum

def mean_subtract(input):
    mean_val = mean(input)
    return [input_i - mean_val for input_i in input]

def variance(input):
    length = len(input)
    deviation = mean_subtract(input)
    return sum_of_squares(deviation) / (length - 1)

print(variance(number_of_laptops))

print()
print("Standard  Deviation = ")
def standard_dev(input):
    return math.sqrt(variance(input))

print(standard_dev(number_of_laptops))

