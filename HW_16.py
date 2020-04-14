import os
import shutil
import pathlib

## Создайте через питон с помощью каждой из библиотек, которые это позволяют, папку, переместите туда файл (например,
# Lord_of_a_Thousand_Suns), скопируйте в папку ещё файлов с помощью какого-нибудь паттерна, переименуйте какой-нибудь
# из них, выведите содержимое этой папки и удалите её (10 баллов за каждый из вариантов)

os.getcwd() #'C:\\Users\\Ekaterina\\Documents\\Bio\\IB\\Python\\Python_HW'
# 1
os.makedirs('my_dir')

os.replace('Lord_of_a_Thousand_Suns.txt', 'my_dir/Lord_of_a_Thousand_Suns.txt')

os.popen('copy ftps.txt ftps2.txt') # do the copy of the in the same directory
os.replace('ftps2.txt', 'my_dir/ftps2.txt') # move to my_dir
os.rename('my_dir/ftps2.txt', 'my_dir/ftps.txt') # rename the file (looks like I copied ftps.txt to my_dir)

os.system('copy ftpss.txt ftpss2.txt') # the same by another option
os.replace('ftpss2.txt', 'my_dir/ftpss2.txt') # move to my_dir
os.rename('my_dir/ftpss2.txt', 'my_dir/ftpss.txt') # rename the file (looks like I copied ftpss.txt to my_dir)

os.listdir('my_dir') # ['ftps.txt', 'ftpss.txt', 'Lord_of_a_Thousand_Suns.txt']

for i in os.scandir(path='my_dir'): # clean up the directory by removing all files
    os.remove(i.path)

os.rmdir('my_dir') # remove the empty directory


#2
os.mkdir('test_dir', 0o777) # I didn't find how to do that by shutil
shutil.move('Lord_of_a_Thousand_Suns.txt', 'test_dir/Lord_of_a_Thousand_Suns.txt') # Move file
shutil.copy2('ftps.txt', 'test_dir/ftps.txt') # Copy file (Identical to copy() except that copy2() also attempts to preserve file metadata.)
shutil.copy('ftpss.txt', 'test_dir/ftpss.txt') # Another one
shutil.move('test_dir/ftpss.txt', 'test_dir/renamed.txt') # Rename file
os.listdir('test_dir') # I didn't find how to do that by shutil
# ['ftps.txt', 'Lord_of_a_Thousand_Suns.txt', 'renamed.txt']
shutil.rmtree('test_dir')

#3
p = pathlib.Path('the_third_direct')
p.mkdir(mode=0o777, parents=False, exist_ok=True)
shutil.copy('ftpss.txt', f'{p}/ftpss.txt')
shutil.copy('ftps.txt', f'{p}/ftps.txt')
shutil.move('Lord_of_a_Thousand_Suns.txt', f'{p}/Lord_of_a_Thousand_Suns.txt')
file = pathlib.Path('the_third_direct/Lord_of_a_Thousand_Suns.txt')
file.replace(f'{p}/new_name.txt')
os.listdir(p) # ['ftps.txt', 'ftpss.txt', 'new_name.txt']

for i in p.iterdir(): # clean up the directory by removing all files
    i.unlink()

p.rmdir() # remove the empty directory