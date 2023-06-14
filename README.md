# Markdown File Search
 This Python script allows you to search for text within Markdown (MD) files in a specified folder and its subfolders.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the `md_search.py` script file.

2. Open a terminal or command prompt and navigate to the folder containing the `md_search.py` script.

3. Run the script with the following command:
```bash
python md_search.py "search term" /path/to/project/folders

```
Replace `"search term"` with the term you want to search for and `/path/to/project/folders` with the path to your project folders.

For example:
```
python md_search.py "grep -oP" C:\mynotes\hacking

```

4. The script will search for the provided term within the MD files in the specified folder and its subfolders. It will print the paths of the files where a match is found along with the matching lines.

## Customization

- If you want to modify or enhance the functionality of the script, feel free to edit the `md_search.py` file.

- You can customize the regular expression patterns used for searching by modifying the `search_md_files` function in the script.

## License

This project is licensed under the [MIT License](LICENSE).



