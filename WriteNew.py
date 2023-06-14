import os

folder_path = input('Please enter the root of your sector: ')

text_to_append = '''
LastSession\tatis_letter0\t 65
LastSession\tatis_url0\thttp://127.0.0.1:11452/atis?icao=$atisairportA&dep_rwy=$deprwy($atisairportA)&arr_rwy=$arrrwy($atisairportA)&code=$atiscodeA&apptype=IDM&arr_oprt=I&dep_oprt=I&is_auto=1
LastSession\tatis_letter1\t 65
LastSession\tatis_url1\thttp://127.0.0.1:11452/atis?icao=$atisairportB&dep_rwy=$deprwy($atisairportB)&arr_rwy=$arrrwy($atisairportB)&code=$atiscodeB&apptype=IDM&arr_oprt=I&dep_oprt=I&is_auto=1
LastSession\tatis_letter2\t 65
LastSession\tatis_url2\thttp://127.0.0.1:11452/atis?icao=$atisairportC&dep_rwy=$deprwy($atisairportC)&arr_rwy=$arrrwy($atisairportC)&code=$atiscodeC&apptype=IDM&arr_oprt=I&dep_oprt=I&is_auto=1
LastSession\tatis_letter3\t 65
LastSession\tatis_url3\thttp://127.0.0.1:11452/atis?icao=$atisairportD&dep_rwy=$deprwy($atisairportD)&arr_rwy=$arrrwy($atisairportD)&code=$atiscodeD&apptype=IDM&arr_oprt=I&dep_oprt=I&is_auto=1
'''

# 获取文件夹内所有以.prf为后缀名的文件
file_list = [file for file in os.listdir(folder_path) if file.endswith('.prf')]

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