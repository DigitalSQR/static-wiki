import os
import re

def is_border_line(line):
    return re.match(r'^\+-[-+]+-\+$', line.strip())

def is_table_row(line):
    return line.strip().startswith('|') and line.strip().endswith('|')

def clean_row(line):
    # Remove leading/trailing | and extra spacing
    return '| ' + ' | '.join(cell.strip() for cell in line.strip()[1:-1].split('|')) + ' |'

def convert_ascii_table(lines):
    result = []
    header_added = False
    for line in lines:
        if is_border_line(line):
            continue
        if is_table_row(line):
            cleaned = clean_row(line)
            result.append(cleaned)
            if not header_added:
                cols = len(cleaned.split('|')) - 2  # exclude empty start/end
                result.append('| ' + ' | '.join(['---'] * cols) + ' |')
                header_added = True
    return result

def fix_tables_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    buffer = []
    in_table = False

    for line in lines:
        if is_border_line(line):
            if not in_table:
                in_table = True
                buffer = []
            continue
        elif in_table and not is_table_row(line):
            # end of table
            new_lines += convert_ascii_table(buffer)
            new_lines.append(line)
            buffer = []
            in_table = False
        elif in_table:
            buffer.append(line)
        else:
            new_lines.append(line)

    # flush last table if file ends with one
    if in_table and buffer:
        new_lines += convert_ascii_table(buffer)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def fix_all_tables(base_dir="docs"):
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                fix_tables_in_file(os.path.join(root, file))

fix_all_tables()
print("✅ Clean table conversion complete.")
