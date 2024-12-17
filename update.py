import os
import time
time.sleep(10)
print('doi xong ')
folder_build = r'D:\1_GITHUB\TEST\Build'
for file in os.listdir(folder_build):
    file_path = os.path.join(folder_build, file)
    if os.path.isfile(file_path):
        if file_path.endswith('exe'):
            folder_bin = r'D:\1_GITHUB\TEST\BIN'
            for file1 in os.listdir(folder_bin):
                file1_path = os.path.join(folder_bin, file1)
                if file1.endswith('exe'):
                    os.remove(file1_path)
                    print(f"File: {file1}")


