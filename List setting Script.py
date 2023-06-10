# 修改Lists指向
print('List setting Script')
import os

search_path = input('Please Enter the sector path:')
target_strings = [
    'Settings\tSettingsfileSIL\t\All\Settings\Lists.txt',
    'Settings\tSettingsfileSEL\t\All\Settings\Lists.txt',
    'Settings\tSettingsfileDEP\t\All\Settings\Lists.txt'
]
replacement_strings = [
    'Settings\tSettingsfileSIL\t\All\Settings\Lists - Tower or below.txt',
    'Settings\tSettingsfileSEL\t\All\Settings\Lists - Tower or below.txt',
    'Settings\tSettingsfileDEP\t\All\Settings\Lists - Tower or below.txt'
]

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('_TWR.prf'):
            file_path = os.path.join(root, file)
            updated_lines = []
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    updated_line = line
                    for target_string, replacement_string in zip(target_strings, replacement_strings):
                        if target_string in line:
                            updated_line = line.replace(target_string, replacement_string)
                            break
                    updated_lines.append(updated_line)

            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
print('Mission Complete.')