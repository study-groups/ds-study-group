import os
import subprocess

# Define the types of files to process differently
code_files = ('.py', '.js', '.html', '.css', '.txt', '.csv')
data_files = ()

def list_directory(directory):
    """
    Uses ls to list the directory contents, including hidden files.
    This function is Unix/Linux/MacOS specific.
    """
    cmd = ['ls', '-1a', directory]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return result.stdout.splitlines()

def process_file(file_path, output_file):
    """Process each file based on its extension."""
    _, ext = os.path.splitext(file_path)
    try:
        if ext in code_files or ext in data_files:
            # For code and data files, include the content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                header = f"## {os.path.basename(file_path)} ##\n" if ext in code_files else ""
                output_file.write(f"{header}{content}\n\n")
        else:
            # For other files, just list the file name and location
            output_file.write(f"{file_path}\n")
    except Exception as e:
        # Handle potential errors in reading files, e.g., permission issues
        output_file.write(f"Error processing file {file_path}: {e}\n")

def build_tree(directory, output_file, prefix=''):
    """
    Recursively builds a visual tree of the directory structure, lists contents,
    and processes files based on their type.
    """
    entries = list_directory(directory)
    for entry in entries:
        if entry in ['.', '..']:
            continue  # Skip the current and parent directory markers
        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            # Directory: write its name and explore it recursively
            output_file.write(f"{prefix}+-- {entry}/\n")
            build_tree(path, output_file, prefix=prefix + "    ")
        else:
            # File: process it based on its type
            output_file.write(f"{prefix}+-- {entry}\n")
            process_file(path, output_file)

def main():
    tree_output_filename = "_directory_tree.txt"
    final_output_filename = "directory_structure_and_files.txt"
    current_directory = os.getcwd()

    # Run the tree command and output the result to a temporary file
    with open(tree_output_filename, "w") as tree_output_file:
        subprocess.run(["tree", "-a", current_directory], stdout=tree_output_file, text=True)

    # Now, build the directory structure and files content
    with open(final_output_filename, "w") as final_output_file:
        # First, write the tree command output
        with open(tree_output_filename, "r") as tree_output_file:
            final_output_file.write(tree_output_file.read())

        # Then, append the detailed directory structure and files content
        build_tree(current_directory, final_output_file)

    # Cleanup the temporary tree output file if needed
    os.remove(tree_output_filename)

    print(f"Combined directory tree and structure with files have been written to {final_output_filename}")

if __name__ == "__main__":
    main()