import os
import re
import argparse

def search_md_files(search_term, folder_path):
    # Compile the search term as a regular expression pattern
    pattern = re.compile(search_term, re.IGNORECASE)

    # Iterate through all the MD files in the specified folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as md_file:
                    # Read the content of the MD file
                    content = md_file.readlines()

                    # Search for the pattern in the MD file content
                    for line_number, line in enumerate(content, start=1):
                        if re.search(pattern, line):
                            print(f"Found '{search_term}' in: {file_path}")
                            print(f"Line {line_number}: {line.strip()}\n")

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Search MD files in project folders.')
parser.add_argument('search_term', type=str, help='the term to search for')
parser.add_argument('folder_path', type=str, help='the path to the project folder')
args = parser.parse_args()

# Call the search function with the provided arguments
search_md_files(args.search_term, args.folder_path)
