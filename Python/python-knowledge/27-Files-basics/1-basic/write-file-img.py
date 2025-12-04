

# CRUCIAL: make sure you have create the file folder before! E.g. "uploads" folder


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Write (save/upload) an image file (with no additional features):
# ATTENTION: this file path below starts from the Python root folder always!
with open("uploads/temp_image.jpg", mode="wb") as file:  # wb = write binary
    file.write(image_data)  # image_data must be bytes



# Write image in chunks (memory-efficient for large files) througt a function:
def store_file(file):
    # ATTENTION: this file path below starts from the Python root folder always!
    with open("uploads/temp_image.jpg", "wb+") as dest:  # wb+ = write binary and read it
        for chunk in file.chunks():
            dest.write(chunk)



# The same function as above but with a few upload validations:
import os
from datetime import datetime

def store_file(file):
    """
    Store uploaded file with datetime prefix and validation.
    Args:
        file: File-like object with .read() method and .name attribute
    Returns:
        str: Path to saved file
    Raises:
        ValueError: If file validation fails
    """
    # Define allowed extensions and max size
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}
    MAX_MB = 10  # Maximum upload file size in megabytes (MB).
    MAX_FILE_SIZE = MAX_MB * 1024 * 1024  # Converting to bytes! 1MB=1024KB×1024bytes=1,048,576bytes
    
    # Extract original filename and extension
    original_filename = getattr(file, 'name', 'unknown')
    filename, extension = os.path.splitext(original_filename)
    extension = extension.lower()
    
    # Validate extension
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Invalid file extension '{extension}'. "
            f"Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Validate file size
    file.seek(0, os.SEEK_END)  # Move cursor to end
    file_size = file.tell()  # Get position (= file size)
    file.seek(0)  # Reset cursor to beginning
    
    if file_size > MAX_FILE_SIZE:
        raise ValueError(
            f"File too large ({file_size / 1024 / 1024:.2f}MB). "
            f"Maximum size: {MAX_MB}MB"
        )
    
    # Generate datetime prefix (format: YYYYMMDD_HHMMSS)
    datetime_prefix = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Build new filename with prefix
    new_filename = f"{datetime_prefix}_{filename}{extension}"
    # ATTENTION: this file path below starts from the Python root folder always!
    file_path = os.path.join("uploads", new_filename)
    
    # Ensure uploads directory exists
    os.makedirs("uploads", exist_ok=True)
    
    # Write file in chunks
    chunk_size = 8192  # 8KB chunks
    with open(file_path, "wb") as dest:
        while chunk := file.read(chunk_size):
            dest.write(chunk)
    
    return file_path