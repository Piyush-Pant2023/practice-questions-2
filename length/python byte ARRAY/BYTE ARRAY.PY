# Create a byte array with some initial values
byte_array = bytearray([10, 20, 30, 40, 50])

# Print the initial byte array
print("Initial byte array:", byte_array)

# Add an element to the byte array
byte_array.append(60)
print("Byte array after appending 60:", byte_array)

# Retrieve and print elements from the byte array
print("Element at index 0:", byte_array[0])
print("Element at index 3:", byte_array[3])
print("Element at the last index:", byte_array[-1])

# Update an element in the byte array
byte_array[2] = 35
print("Byte array after updating index 2 to 35:", byte_array)

# Iterate over the byte array and print each element
print("Iterating over the byte array:")
for i, byte in enumerate(byte_array):
    print(f"Element at index {i}: {byte}")
