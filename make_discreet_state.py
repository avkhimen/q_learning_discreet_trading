import numpy as np

num_divisions = 200
num_states = 3

random_state = np.random.random((num_states, num_divisions))

print(random_state)

# Your input numpy array with arbitrary shape
input_array = random_state

# Define the ranges and their corresponding labels
start = 0.9
end = 1.1

# Calculate the step size based on the number of divisions
step = (end - start) / num_divisions

# Generate the ranges dictionary
ranges = {i: [start + i * step, start + (i + 1) * step] for i in range(num_divisions)}

# Print the ranges dictionary
print(ranges)

# Function to convert a single value to its corresponding label based on ranges
def convert_to_labels(value, ranges):
    for label, (start, end) in ranges.items():
        if start <= value < end:
            return label
    return None

# Function to apply conversion to numpy arrays of arbitrary shape
def convert_array(input_array, ranges):
    if isinstance(input_array, (int, float)):
        return convert_to_labels(input_array, ranges)
    elif isinstance(input_array, np.ndarray):
        return np.vectorize(lambda x: convert_array(x, ranges))(input_array)
    else:
        raise ValueError("Unsupported input type")

# Apply the conversion to the input_array
output_array = convert_array(input_array, ranges)

print(output_array)