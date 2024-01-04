import numpy as np

sh = (5,5,5)

random_state = np.random.random(sh)

print(random_state)

import numpy as np

# Your input numpy array with arbitrary shape
input_array = random_state

# Define the ranges and their corresponding labels
ranges = {
    0: [0, 0.1],
    1: [0.1, 0.2],
    2: [0.2, 0.3],
    3: [0.3, 0.4],
    4: [0.4, 0.5],
    5: [0.5, 0.6],
    6: [0.6, 0.7],
    7: [0.7, 0.8],
    8: [0.8, 0.9],
    9: [0.9, 1]
}

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