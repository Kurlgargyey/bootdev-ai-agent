import os

def get_file_content(working_directory, file_path):
    result = f"Result for '{file_path}\n"

    if not os.path.isfile(file_path):
        error = f'Error: File not found or is not a regular file: "{file_path}"'
        result += error
        return result
    if not os.path.commonpath(working_directory, file_path) == working_directory:
        error = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        result += error
        return result
    MAX_CHARS = 10000
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
