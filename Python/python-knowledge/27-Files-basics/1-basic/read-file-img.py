# Read (load) an image file
# ATTENTION 1: No encoding parameter: Binary data doesn't need text encoding.
# ATTENTION 2: this file path below starts from the Python root folder always!
with open("imgs/image.jpg", mode="rb") as file:  # rb = read binary
    image_data = file.read()  # Returns bytes object


# Read image in chunks (memory-efficient for large files)
# ATTENTION 1: No encoding parameter: Binary data doesn't need text encoding.
# ATTENTION 2: this file path below starts from the Python root folder always!
with open("imgs/image.jpg", mode="rb") as file:  # rb = read binary
    while chunk := file.read(8192):  # Read 8KB at a time
        process(chunk)