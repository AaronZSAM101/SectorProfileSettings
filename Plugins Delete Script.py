# 批量删除插件
print('Plugins Delete Script')
import os

search_path = input('Please enter your Sector Path:')
target_strings = [
    'Plugins\tPlugin7\t\All\Plugins\VATCANBookings.dll',
    'Plugins\tPlugin7Display0\tSMR radar display',
    'Plugins\tPlugin7Display1\tStandard ES radar screen'
]

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('_APP.prf'):
            file_path = os.path.join(root, file)
            updated_lines = []
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if all(target_string not in line for target_string in target_strings):
                        updated_lines.append(line)

            with open(file_path, 'w') as f:
                f.writelines(updated_lines)
print('Mission Complete.')