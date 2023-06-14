import os

folder_path = input('Please enter the root of your sector: ')

text_to_append = '''
Settings	alias	\All\Settings\Alias.txt
'''

# 获取文件夹内所有以.prf为后缀名的文件
file_list = [file for file in os.listdir(folder_path) if file.endswith('_TWR.prf')]

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    
    try:
        # 在文件末尾追加文本内容
        with open(file_path, 'a') as file:
            file.write(text_to_append)
        
        print(f"Appended content to file: {file_name}")
    
    except Exception as e:
        print(f"Failed to append content to file: {file_name}. Error: {str(e)}")

print("Mission Complete.")