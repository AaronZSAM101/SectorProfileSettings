# 完成后请用GBK保存！
import os
import re
# 定义路径
Sector_PATH=input('请输入扇区路径：')
# Personalfile_PATH=input('请输入个人配置文件的路径：')

# 定义个人信息
realname=input('请输入登陆时显示的名字：')
cid=input('请输入你的VATSIM CID：')
password=input('请输入你的密码：')
print('等级：S1-"1" S2-"2" S3-"3" C1-"4" C3-"6" I1-"7" I3-"9" SUP-"10"')
rating=input('请输入你的等级：')


# 对扇区文件进行操作
## 修改个人信息
target_lines = '''LastSession\trealname\tTiansuo Li\nLastSession\tcertificate\t114514\nLastSession\tpassword\t1145141919810'''
replace_lines = f'''LastSession\trealname\t{realname}\nLastSession\tcertificate\t{cid}\nLastSession\tpassword\t{password}'''
## 对已存在的个人信息进行替换
escaped_target_content = re.escape(target_lines)
for root, dirs, files in os.walk(Sector_PATH):
    for file in files:
        if file.endswith('.prf'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()

            # Perform the replacement using regular expression
            updated_content = re.sub(escaped_target_content, replace_lines, content)

            with open(file_path, 'w') as f:
                f.write(updated_content)
## 对未存在个人信息的prf写入个人信息
def process_file(Sector_PATH):
    with open(Sector_PATH,'.prf','r') as file:
        content = file.read()
    if 'LastSession\trealname\tTiansuo Li\nLastSession\tcertificate\t114514\nLastSession\tpassword\t1145141919810' not in content:
        with open(file_path, 'a') as file:
            file.write(f"LastSession\trealname\t{realname}\nLastSession\tcertificate\t{cid}\nLastSession\tpassword\t{password}\n")
# file.write()
print('个人信息修改完成！')

## 修改Topsky的CPDLC Logon Code
TopskyPath=input('请输入Topsky插件的目录：')
logon_code=input('请输入你的CPDLC Logon Code：')
with open(os.path.join(TopskyPath, "TopSkyCPDLChoppieCode.txt"), 'a') as f:
    f.write(f"{logon_code}")
print("CPDLC Logon Code 修改完成！")
input("扇区配置完成！")