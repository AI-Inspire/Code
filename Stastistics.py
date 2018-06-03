#STATISTICS
number_of_laptops = [30, 40, 50, 60, 311, 23, 13]
num_points = len(number_of_laptops) #number of data points, length
largest_value = max(number_of_laptops) #largest value
#sorting values
sorted_values = sorted(number_of_laptops)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
third_largest_value = sorted_values[-3]

print(sorted_values,"\n")
print(smallest_value,"\n")
print(second_smallest_value,"\n")
print(third_largest_value,"\n")
print(largest_value,"\n")

