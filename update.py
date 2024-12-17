import os
folder_build = r'D:\1_GITHUB\TEST\Build'
for file in os.listdir(folder_build):
    file_path = os.path.join(folder_build, file)
    if os.path.isfile(file_path):  # Kiểm tra nếu là file
        print(f"File: {file_path}")


import psutil

def kill_process_by_name(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == process_name:
            print(f"Đang dừng tiến trình: {proc.info['name']} (PID: {proc.info['pid']})")
            proc.kill()
            return True
    print(f"Không tìm thấy tiến trình: {process_name}")
    return False

# Buộc dừng GUI.exe
if not kill_process_by_name("GUI_v4.py"):
    kill_process_by_name("python.exe")
def schedule_self_deletion(self,folder_build):

    current_file = os.path.join(folder_build,"update.py")
    delete_script_path = os.path.join(folder_build, "delete_self.bat")


    with open(delete_script_path, "w") as f:
        f.write('@echo off\n')
        f.write('timeout /t 2 > nul\n')  
        f.write(f'del "{current_file}" > nul\n')  
        f.write(f'del "{delete_script_path}" > nul\n') 
        f.write('exit\n')


    subprocess.Popen(delete_script_path, shell=True)

    sys.exit(0)
