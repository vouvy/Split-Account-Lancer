import re
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
name_file = 'name.txt'
old_file = 'old.txt'
new_file = 'new.txt'
lancer_names = extract_lancer_names(name_file)
print(f'Extracted lancer names: {lancer_names}')
filtered_lines = filter_old_file(lancer_names, old_file)
print(f'Filtered lines: {filtered_lines}')
write_new_file(filtered_lines, new_file)
print(f'Filtered lines written to {new_file}')
