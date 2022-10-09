import os

def create_output_directory():
    directory = "output_dir"
    # Create the directory
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass



