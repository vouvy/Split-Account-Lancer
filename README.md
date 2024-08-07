<h1 align="center">
<table>
<tr>
<td>
This script is a basic example of the Python programming language It was created for personal use But feel free to use or study it
</td>
</tr>
</table>

---

<h1 align="center">
  <br>
  Features
  <br>
</h1>

> [!NOTE]  
> **This program is not designed for everyone It might seem a bit confusing I will update the program to make it more user-friendly and visually appealing next time**

- File Deletion: The delete_files function takes a list of file paths and deletes those files if they exist. If a file doesn't exist, it reports that as well.
- File Creation: The create_file function creates a new file. If the file doesn't exist, it prompts the user to enter data line by line until they type 'done'. The data is then written to the file.
- Read File Data: The get_file_data function reads the contents of a file and returns it as a list of lines.
- Extract Lancer Names: The extract_lancer_names function looks for names in a file that match a specific pattern (Lancer followed by six digits) and collects these names into a list.
- Filter Old File: The filter_old_file function reads lines from an old file and keeps only those that contain names from the list of lancer names. It returns these filtered lines.
- Write New File: The write_new_file function writes the filtered lines to a new file.
- Main Function: The main function coordinates the overall process. It deletes existing files, creates new ones, extracts lancer names from one file, filters lines from an old file based on these names, and writes the filtered results to a new file. Finally, it waits for the user to press Enter before exiting.

---

<h1 align="center">
  <br>
  How To Use
  <br>
</h1>

![screenshot](https://github.com/vouvy/Split-Account-Lancer/blob/main/Img/Split-Account-Lancer.gif?raw=true)

> [!TIP]
> **If message is "Filtered lines written to New_Name.txt", you can check the file New_Name.txt to see the results**

> [!TIP]
> **If message is [''], it indicates that you have entered incorrect information**

---

<h1 align="center">
  <br>
  Code Example
  <br>
</h1>

```python
import os  # Importing the os module for file operations
import re  # Importing the re module for regular expression operations

# Function to delete files if they exist
def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):  # Check if the file exists
            os.remove(file_path)  # Remove the file
            print(f"{file_path} has been deleted.")  # Print confirmation message
        else:
            print(f"{file_path} does not exist.")  # Print message if the file does not exist

# Function to create a file and write user input into it
def create_file(file_path):
    print(f"{file_path} does not exist. Creating {file_path}.")  # Inform user that the file is being created
    with open(file_path, 'w', encoding='utf-8') as f:  # Open the file in write mode
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")  # Get user input
            if line.lower() == 'done':  # If user types 'done', exit the loop
                break
            f.write(line + '\n')  # Write the input to the file, followed by a newline

# Function to read data from a file and return it as a list of lines
def get_file_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:  # Open the file in read mode
        return f.read().splitlines()  # Read the file content and split into lines

# Function to extract names matching the pattern 'Lancer' followed by 6 digits
def extract_lancer_names(name_file):
    lancer_names = []  # List to store extracted names
    lancer_pattern = re.compile(r'Lancer\d{6}')  # Regular expression pattern for 'Lancer' followed by 6 digits
    with open(name_file, 'r', encoding='utf-8') as file:  # Open the file in read mode
        for line in file:  # Iterate over each line in the file
            match = lancer_pattern.search(line)  # Search for the pattern in the line
            if match:
                lancer_names.append(match.group())  # If a match is found, add it to the list
    return lancer_names  # Return the list of names

# Function to filter lines from an old file based on names in a list
def filter_old_file(names, old_file):
    filtered_lines = []  # List to store filtered lines
    with open(old_file, 'r', encoding='utf-8') as file:  # Open the old file in read mode
        old_data = file.readlines()  # Read all lines from the old file
        for name in names:  # For each name in the list of names
            for line in old_data:  # Check each line in the old file
                if name in line:  # If the name is found in the line
                    filtered_lines.append(line.strip())  # Add the line to the filtered lines list
                    break  # Move to the next name
    return filtered_lines  # Return the list of filtered lines

# Function to write filtered lines to a new file
def write_new_file(filtered_lines, new_file):
    with open(new_file, 'w', encoding='utf-8') as file:  # Open the new file in write mode
        for line in filtered_lines:  # For each line in the filtered lines
            file.write(line + '\n')  # Write the line to the new file, followed by a newline

# Main function to execute the workflow
def main():
    name_file = 'Check_Name.txt'  # Define the name of the file to create and extract names from
    old_file = 'Old_Name.txt'  # Define the name of the old file to filter lines from
    new_file = 'New_Name.txt'  # Define the name of the new file to write filtered lines to
    delete_files([name_file, old_file, new_file])  # Delete existing files
    create_file(name_file)  # Create the name file and populate it with user input
    create_file(old_file)  # Create the old file and populate it with user input
    lancer_names = extract_lancer_names(name_file)  # Extract lancer names from the name file
    print(f'Extracted lancer names: {lancer_names}')  # Print the extracted names
    filtered_lines = filter_old_file(lancer_names, old_file)  # Filter lines from the old file based on extracted names
    print(f'Filtered lines: {filtered_lines}')  # Print the filtered lines
    write_new_file(filtered_lines, new_file)  # Write the filtered lines to the new file
    print(f'Filtered lines written to {new_file}')  # Print confirmation that lines were written
    input("Press Enter to exit...")  # Wait for user input before exiting

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
```
