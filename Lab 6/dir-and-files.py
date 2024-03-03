#1
#1.1List Only Directories
import os

def list_only_directories(path):
    """
    Lists only directories in the specified path.
    """
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isdir(full_path):
            print(f"Directory: {full_path}")

# specified_path = r'C:\Users\timur\Documents\GitHub'
# print("Directories:")
# list_only_directories(specified_path)

#1.2List Files and All Directories:
def list_files_and_all_directories(path):
    """
    Lists files and all directories in the specified path.
    """
    for root, dirs, files in os.walk(path):
        for name in dirs:
            print(f"Directory: {os.path.join(root, name)}")
        for name in files:
            print(f"File: {os.path.join(root, name)}")

# specified_path = r'C:\Users\timur\Documents\GitHub'
# print("Files and All Directories:")
# list_files_and_all_directories(specified_path)

#1.3List Files Only import os
def list_files(path):
    """
    Lists files in the specified path.
    """
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            print(f"File: {full_path}")


# specified_path = r'C:\Users\timur\Documents\GitHub'
# print("Files:")
# list_files(specified_path)

#2
def check_path_access(path):
    """
    Checks the existence, readability, writability, and executability of the specified path.
    """
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        if os.access(path, os.R_OK):
            print(f"Read permission granted for '{path}'.")
        else:
            print(f"Read permission denied for '{path}'.")
        if os.access(path, os.W_OK):
            print(f"Write permission granted for '{path}'.")
        else:
            print(f"Write permission denied for '{path}'.")
        if os.access(path, os.X_OK):
            print(f"Execute permission granted for '{path}'.")
        else:
            print(f"Execute permission denied for '{path}'.")
    else:
        print(f"Path '{path}' does not exist.")

# specified_path = r'C:\Users\timur\Documents\GitHub'
# check_path_access(specified_path)
#3
def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")


# given_path = r'C:\Users\timur\Documents\GitHub'
# check_path(given_path)

#4
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0

# text_file_path = "sample.txt"
# line_count = count_lines_in_file(text_file_path)
# print(f"Number of lines in {text_file_path}: {line_count}")

#5
def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + "\n")
        print(f"List written to {file_path} successfully.")
    except Exception as e:
        print(f"Error writing list to {file_path}: {e}")

# my_list = ["apple", "banana", "cherry", "date"]
# output_file_path = "output_list.txt"
# write_list_to_file(output_file_path, my_list)

#6
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is the content of {filename}\n")
    print(f"File {filename} created.")

print("26 text files created successfully.")

#7
def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
            with open(destination_path, 'w') as destination_file:
                destination_file.write(content)
        print(f"Contents of {source_path} successfully copied to {destination_path}.")
    except FileNotFoundError:
        print(f"Error: File {source_path} not found.")

# source_file_path = "source.txt"
# destination_file_path = "destination.txt"
# copy_file(source_file_path, destination_file_path)

#8
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted successfully.")
            else:
                print(f"You do not have write access to '{file_path}'.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

# file_to_delete = "file_to_delete.txt"
# delete_file(file_to_delete)


