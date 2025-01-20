import os
import shutil
import time
import subprocess
import sys
# Tạo một file log để lưu lỗi


# Hàm ghi ngoại lệ vào file log
def log_error(message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(message + '\n')

# Đảm bảo đợi đủ lâu trước khi thực thi xóa
#time.sleep(2)


#folder_build = r'D:\1_GITHUB\TEST\Build'
#folder_bin = r'D:\1_GITHUB\TEST\BIN'
# Xóa file .exe trong folder_bin
#for file in os.listdir(folder_bin):
#    file_path = os.path.join(folder_bin, file)
#    if os.path.isfile(file_path) and file_path.endswith('.exe'):
#        try:
#            # Kiểm tra nếu file đang sử dụng, sau đó xóa
#            os.remove(file_path)
#            print(f"Đã xóa file: {file_path}")
#        except PermissionError as e:
#            error_message = f"Không thể xóa file {file_path} do lỗi quyền truy cập: {str(e)}"
#            print(error_message)
#            log_error(error_message)  # Ghi lỗi vào file log
#        except Exception as e:
#            error_message = f"Không thể xóa file {file_path} do lỗi: {str(e)}"
#            print(error_message)
#            log_error(error_message)  # Ghi lỗi vào file log






def schedule_self_deletion(folder_del):

    current_file = os.path.join(folder_del,"update.py")
    delete_script_path = os.path.join(folder_del, "delete_self.bat")


    with open(delete_script_path, "w") as f:
        f.write('@echo off\n')
        f.write('timeout /t 2 > nul\n')  
        f.write(f'del "{current_file}" > nul\n')  
        f.write(f'del "{delete_script_path}" > nul\n') 
        f.write('exit\n')


    subprocess.Popen(delete_script_path, shell=True)

    sys.exit(0)

if __name__ == '__main__':
    folder_del = sys.argv[1]
    schedule_self_deletion(folder_del)
