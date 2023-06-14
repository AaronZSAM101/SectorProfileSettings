# 批量写入
print('Writing Script')
import os

search_path = input('Please enter the sector path:')
target_string = 'Settings\tairlines\t\All\ICAO\ICAO_Airlines.txt' # 上一行
new_line = 'Settings\tairportcoords\t\All\ICAO\icao.txt' # 新行（要新写的）

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('.prf'):
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