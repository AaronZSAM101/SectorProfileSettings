# 批量写入（在行中操作）
print('Writing Script')
import os

search_path = input('Please enter the root of your sector: ')
target_string = ['LastSession\tconnecttype\t0']
new_line = ['LastSession\tcallsign\tClick here ---------------->']

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('.prf'):
            file_path = os.path.join(root, file)
            updated_lines = []
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    updated_lines.append(line)
                    if all(item in line for item in target_string):
                        updated_lines.append(''.join(new_line) + '\n')

            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
print('Mission Complete.')