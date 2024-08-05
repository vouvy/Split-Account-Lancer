<table>
<tr>
<td>
This script is a basic example of the Python programming language. It was created for personal use, but feel free to use or study it
</td>
</tr>
</table>

---

## Features

- Extract Lancer Names: It reads a file (name_file), searches for patterns matching 'Lancer' followed by six digits (e.g., 'Lancer123456') using a regular expression, and collects these names into a list.
- Filter Old File: It reads another file (old_file) and filters out lines that contain any of the names extracted in the previous step. The filtered lines are stored in a list.
- Write New File: It writes the filtered lines to a new file (new_file), each line on a new line in the file.

## Code Example:

```python
import re  # Import the 're' module for regular expressions.

def extract_lancer_names(name_file):
    lancer_names = []  # Initialize an empty list to store Lancer names.
    lancer_pattern = re.compile(r'Lancer\d{6}')  # Compile a regex pattern to match 'Lancer' followed by 6 digits.
    with open(name_file, 'r', encoding='utf-8') as file:  # Open the file specified by 'name_file' for reading with UTF-8 encoding.
        for line in file:  # Iterate through each line in the file.
            match = lancer_pattern.search(line)  # Search for the Lancer pattern in the current line.
            if match:  # If a match is found,
                lancer_names.append(match.group())  # Append the matched Lancer name to the list.
    return lancer_names  # Return the list of extracted Lancer names.

def filter_old_file(names, old_file):
    filtered_lines = []  # Initialize an empty list to store filtered lines.
    with open(old_file, 'r', encoding='utf-8') as file:  # Open the file specified by 'old_file' for reading with UTF-8 encoding.
        old_data = file.readlines()  # Read all lines from the old file into a list.
        for name in names:  # Iterate through each name in the list of names.
            for line in old_data:  # Iterate through each line in the old file's data.
                if name in line:  # If the current name is found in the line,
                    filtered_lines.append(line.strip())  # Append the line (with leading and trailing whitespace removed) to the filtered lines list.
                    break  # Stop searching for more occurrences of this name in the current line.
    return filtered_lines  # Return the list of filtered lines.

def write_new_file(filtered_lines, new_file):
    with open(new_file, 'w', encoding='utf-8') as file:  # Open the file specified by 'new_file' for writing with UTF-8 encoding.
        for line in filtered_lines:  # Iterate through each line in the filtered lines list.
            file.write(line + '\n')  # Write the line to the new file, followed by a newline character.

name_file = 'name.txt'  # Specify the file containing names to extract.
old_file = 'old.txt'  # Specify the old file to filter lines from.
new_file = 'new.txt'  # Specify the new file to write filtered lines to.

lancer_names = extract_lancer_names(name_file)  # Call the function to extract Lancer names from the specified file.
print(f'Extracted lancer names: {lancer_names}')  # Print the list of extracted Lancer names.

filtered_lines = filter_old_file(lancer_names, old_file)  # Call the function to filter lines from the old file based on the extracted Lancer names.
print(f'Filtered lines: {filtered_lines}')  # Print the list of filtered lines.

write_new_file(filtered_lines, new_file)  # Call the function to write the filtered lines to the new file.
print(f'Filtered lines written to {new_file}')  # Print a confirmation message that the filtered lines have been written to the new file.
```
