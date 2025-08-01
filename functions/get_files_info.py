import os
def get_files_info(working_directory, directory="."):
    print(f"Result for {directory} directory:")
    target_dir = os.path.normpath(os.path.abspath(os.path.join(working_directory, directory)))
    working_directory = os.path.abspath(working_directory)
    
    if not os.path.isdir(target_dir):
        error = f'Error: "{directory}" is not a directory'
        print(error)
        return error
    if not (os.path.commonpath([working_directory, target_dir])==working_directory):
        error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        print(error)
        return error
        
    contents = os.listdir(target_dir)
    for file in contents:
        subpath = os.path.join(target_dir, file)
        print(f" - {file}: file_size={os.path.getsize(subpath)}, is_dir={os.path.isdir(subpath)}")
