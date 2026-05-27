# Copy an image
with open("source.jpg", "rb") as source:
    with open("destination.jpg", "wb") as dest:
        dest.write(source.read())



# Write image in chunks from another file (copy operation)
with open("source.jpg", "rb") as source:
    with open("destination.jpg", "wb") as dest:
        while True:
            chunk = source.read(8192)  # Read 8KB at a time
            if not chunk:  # End of file
                break
            dest.write(chunk)



# More Pythonic version using shutil (recommended for file copying)
import shutil

with open("source.jpg", "rb") as source:
    with open("destination.jpg", "wb") as dest:
        shutil.copyfileobj(source, dest, length=8192)  # Handles chunking automatically