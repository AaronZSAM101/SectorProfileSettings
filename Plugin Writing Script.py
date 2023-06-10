# 批量写入插件
print('Plugin Writing Script')
import os

search_path = input('Please enter the sector path:')
target_string = 'Plugins\tPlugin5Display1\tStandard ES radar screen'
new_line = 'Plugins\tPlugin6\t\All\Plugins\MTEPlugin.dll'

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('_TWR.prf'):
            file_path = os.path.join(root, file)
            updated_lines = []
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    updated_lines.append(line)
                    if target_string in line:
                        updated_lines.append(new_line + '\n')

            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
print('Mission Complete.')