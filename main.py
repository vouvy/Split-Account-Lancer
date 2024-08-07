import os
import re
def delete_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")
def create_file(file_path):
    print(f"{file_path} does not exist. Creating {file_path}.")
    with open(file_path, 'w', encoding='utf-8') as f:
        while True:
            line = input(f"Enter data for {file_path} (type 'done' to finish): ")
            if line.lower() == 'done':
                break
            f.write(line + '\n')
def get_file_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
def extract_lancer_names(name_file):
    lancer_names = []
    lancer_pattern = re.compile(r'Lancer\d{6}')
    with open(name_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = lancer_pattern.search(line)
            if match:
                lancer_names.append(match.group())
    return lancer_names
def filter_old_file(names, old_file):
    filtered_lines = []
    with open(old_file, 'r', encoding='utf-8') as file:
        old_data = file.readlines()
        for name in names:
            for line in old_data:
                if name in line:
                    filtered_lines.append(line.strip())
                    break
    return filtered_lines
def write_new_file(filtered_lines, new_file):
    with open(new_file, 'w', encoding='utf-8') as file:
        for line in filtered_lines:
            file.write(line + '\n')
def main():
    name_file = 'Check_Name.txt'
    old_file = 'Old_Name.txt'
    new_file = 'New_Name.txt'
    delete_files([name_file, old_file, new_file])
    create_file(name_file)
    create_file(old_file)
    lancer_names = extract_lancer_names(name_file)
    print(f'Extracted lancer names: {lancer_names}')
    filtered_lines = filter_old_file(lancer_names, old_file)
    print(f'Filtered lines: {filtered_lines}')
    write_new_file(filtered_lines, new_file)
    print(f'Filtered lines written to {new_file}')
    input("Press Enter to exit...")
if __name__ == "__main__":
    main()
