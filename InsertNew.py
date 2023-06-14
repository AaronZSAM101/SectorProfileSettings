# 批量写入（在行中操作）
print('Writing Script')
import os

search_path = input('Please enter the root of your sector: ')
target_string = ['Settings\tSettingsfilePILOTING\t\All\Settings\Lists.txt']
new_line = ['Settings\tSettingsfileORIGPLANE\t\All\Settings\Lists.txt\n',
            'Settings\tSettingsfileSTUP\t\All\Settings\Lists.txt\n',
            'Settings\tSettingsfileTAXIOUT\t\All\Settings\Lists.txt\n',
            'Settings\tSettingsfileTAKEOFF\t\All\Settings\Lists.txt\n',
            'Settings\tSettingsfileADCS\t\All\Settings\Lists.txt\n',
            'Settings\tSettingsfileTAXIIN\t\All\Settings\Lists.txt']

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