import os

def get_file_content(working_directory, file_path):
    result = f"Result for '{file_path}\n"

    if not os.path.isfile(file_path):
        error = f'Error: File not found or is not a regular file: "{file_path}"'
        result += file_path
        return result
