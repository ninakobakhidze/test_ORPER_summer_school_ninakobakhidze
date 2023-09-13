# Libraries
import numpy as np

#
def calculate_mean(vector):
    if len(vector) == 0:
        return "Vector is empy, cannot compute mean"  # Return None for an empty vector (undefined mean)
    else:
        total = sum(vector)
        mean_of_vector = total / len(vector)
        return mean_of_vector

# Example usage:
vector = [1, 2, 3, 4, 5]
result = calculate_mean(vector)
print("Mean:", result)



def calculate_standard_deviation(vector):
    if len(vector) == 0:
        return "Vector is empy, cannot compute mean"  # Return None for an empty vector (undefined mean)
    else:
        mean_of_vector = calculate_mean(vector)
        standard_deviation_homemade = np.sqrt((sum([value - mean_of_vector for value in vector])**2)/len(vector))
        standard_deviation_np = np.std(vector)
        return standard_deviation_homemade, standard_deviation_np