import os
import shutil
import time

# Tạo một file log để lưu lỗi
log_file_path = r'D:\1_GITHUB\TEST\error_log.txt'

# Hàm ghi ngoại lệ vào file log
def log_error(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(message + '\n')

# Đảm bảo đợi đủ lâu trước khi thực thi xóa
time.sleep(10)
print('Đợi xong')

folder_build = r'D:\1_GITHUB\TEST\Build'
folder_bin = r'D:\1_GITHUB\TEST\BIN'

# Kiểm tra nếu file update.py tồn tại
update_file_path = os.path.join(folder_build, "update.py")
if os.path.exists(update_file_path):
    subprocess.Popen(["python", update_file_path])
    sys.exit()

else:
    # Nếu không có file update.py, xóa toàn bộ folder_build
    if not os.path.exists(update_file_path):
        shutil.rmtree(folder_build)  # Xóa toàn bộ folder_build
        os.makedirs(folder_build)
        print('Không có file update.py')

# Xóa file .exe trong folder_bin
for file in os.listdir(folder_bin):
    file_path = os.path.join(folder_bin, file)
    if os.path.isfile(file_path) and file_path.endswith('.exe'):
        try:
            # Kiểm tra nếu file đang sử dụng, sau đó xóa
            os.remove(file_path)
            print(f"Đã xóa file: {file_path}")
        except PermissionError as e:
            error_message = f"Không thể xóa file {file_path} do lỗi quyền truy cập: {str(e)}"
            print(error_message)
            log_error(error_message)  # Ghi lỗi vào file log
        except Exception as e:
            error_message = f"Không thể xóa file {file_path} do lỗi: {str(e)}"
            print(error_message)
            log_error(error_message)  # Ghi lỗi vào file log





# Buộc dừng GUI.exe
# def schedule_self_deletion(self,folder_build):

#     current_file = os.path.join(folder_build,"update.py")
#     delete_script_path = os.path.join(folder_build, "delete_self.bat")


#     with open(delete_script_path, "w") as f:
#         f.write('@echo off\n')
#         f.write('timeout /t 2 > nul\n')  
#         f.write(f'del "{current_file}" > nul\n')  
#         f.write(f'del "{delete_script_path}" > nul\n') 
#         f.write('exit\n')


#     subprocess.Popen(delete_script_path, shell=True)

#     sys.exit(0)
