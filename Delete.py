# 批量删除
print('Delete Script')
import os

search_path = input('Please enter your Sector Path:')
# 方括号内为你要删除的内容
target_strings = [ 
    'LastSession\tcallsign\tClick here ---------------->',
    'LastSession\trealname\tTiansuo Li',
    'LastSession\tcertificate\t114514',
    'LastSession\tpassword\t1145141919810'
] 

for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith('.prf'):
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