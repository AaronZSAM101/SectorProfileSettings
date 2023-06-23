import os
import shutil
RUDI_SECTOR_Path=input('Please enter the Path of Sector:')
PERSONAL_files_Path=input('Please enter the Path of Personal File :')
# 复制到FSS
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'FSS', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'FSS', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'FSS', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'FSS', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('飞服扇个人配置完成')
# 复制到ZBPE
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZBPE', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZBPE', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZBPE', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZBPE', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZBPE扇个人配置完成')                       
# 复制到ZGZU                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZGZU', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZGZU', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZGZU', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZGZU', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZGZU扇个人配置完成')                       
# 复制到ZJSA                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZJSA', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZJSA', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZJSA', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZJSA', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZJSA扇个人配置完成')                       
# 复制到ZWUQ                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZWUQ扇个人配置完成')                       
# 复制到ZLHW                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZLHW', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZLHW', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZLHW', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZLHW', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZLHW扇个人配置完成')                       
# 复制到ZPKM                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZPKM', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZPKM', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZPKM', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZPKM', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZPKM扇个人配置完成')                       
# 复制到ZSHA                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZSHA', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZSHA', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZSHA', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZSHA', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZSHA扇个人配置完成')                       
# 复制到ZWUQ                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZWUQ', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZWUQ扇个人配置完成')                       
# 复制到ZYSH                                      
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'ESPlaneCounter.dll'),os.path.join(RUDI_SECTOR_Path, 'ZYSH', 'Data', 'Stock', 'Plugins', 'ESPlaneCounter.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'MTEPlugin.dll'),os.path.join(RUDI_SECTOR_Path, 'ZYSH', 'Data', 'Stock', 'Plugins', 'MTEPlugin.dll'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Tag.txt'),os.path.join(RUDI_SECTOR_Path, 'ZYSH', 'Data', 'Stock', 'Settings', 'Tag.txt'))
shutil.copyfile(os.path.join(PERSONAL_files_Path, 'Privat Alias.txt'),os.path.join(RUDI_SECTOR_Path, 'ZYSH', 'Data', 'Stock', 'Settings', 'Privat Alias.txt'))
print('ZYSH扇个人配置完成')
print('Mission Complete.')
