'''
# Categorizes files in the current directory based on their extension
# Does not move any existing directories.
# Categories will be as follows.
# pdf,zip,tar                       -> Documents
# html,xml,css                      -> Web
# msi,exe                           -> Application
# py,js                             -> Code
# jpeg,jpg,png,mov,mp4,mp3,avi      -> Media
'''
import os
import shutil
from pathlib import Path
import time

# get the current directory curr_path(working directory)
curr_path = Path.cwd()

# Predifeined extensions
category = {
            1:'Documents', 
            2:'Web', 
            3:'Application', 
            4:'Code', 
            5:'Media'
            }

sub_category = {
    '.pdf':1, '.zip':1, '.tar':1, '.html':2, '.xml':2, '.css':2, '.msi':3, '.exe':3, '.py':4, '.js':4, '.jpeg':5, '.jpg':5, '.png':5,'.mov':5, '.mp4':5, 'mp3':5, '.avi':5,
    }

# Returns a string abs curr_path of the given filename with the current directory 
def file_path_creator(file_name, path = curr_path):
    return str(path) + '\\' + file_name

exception_files = ['File_handler.py']
exceptions = set()

# Populating exceptions set
for item in exception_files:
    abs_str_path = file_path_creator(item)
    exceptions.add(abs_str_path)


# create categorical directories if not present and move the files in real time to respective directories
def directory_cleaner():
    for f in curr_path.iterdir():

        if f.is_file() and str(f) not in exceptions:
            folder_name = category.get(sub_category.get(f.suffix))
            d = Path(file_path_creator(folder_name))

            if not os.path.exists(d):
                d.mkdir()
            try:
                dst_file = file_path_creator(f.name, d)

                if os.path.exists(dst_file):
                    os.remove(dst_file)

                shutil.move(src = f, dst = d)
                print(f'Done : Moved {f.name} to {d}')
            
            except Exception as e:
                print(e)
                
if __name__ == "__main__":

    print(__doc__)

    start_time = time.time()

    directory_cleaner()

    end_time = time.time()

    print(f'Completed in {end_time - start_time} seconds')


# Author : Ajay Narayanan
# Date   : 19/12/2024
