#create an automation script that can back up files from a folder within 3 minutes of modification to a back  up folder
import os
import shutil
import time
from datetime import datetime, timedelta

# Configure your folders here
SOURCE_FOLDER = r"C:\Users\DELL\Desktop\SIDEWORK"        # <- Change this
BACKUP_FOLDER = r"C:\Users\DELL\Desktop\BACKUP"       # <- Change this
CHECK_INTERVAL_SECONDS = 60  # Check every minute
MODIFICATION_WINDOW_MINUTES = 3

def is_modified_recently(filepath, minutes=3):
    modified_time = datetime.fromtimestamp(os.path.getmtime(filepath))
    return datetime.now() - modified_time <= timedelta(minutes=minutes)

def backup_file(src_file, base_src_folder, base_dst_folder):
    relative_path = os.path.relpath(src_file, base_src_folder)
    dst_file = os.path.join(base_dst_folder, relative_path)

    os.makedirs(os.path.dirname(dst_file), exist_ok=True)
    shutil.copy2(src_file, dst_file)
    print(f"Backed up: {src_file} -> {dst_file}")

def monitor_and_backup():
    print("Monitoring started...")
    while True:
        for foldername, subfolders, filenames in os.walk(SOURCE_FOLDER):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                if is_modified_recently(filepath, MODIFICATION_WINDOW_MINUTES):
                    backup_file(filepath, SOURCE_FOLDER, BACKUP_FOLDER)
        time.sleep(CHECK_INTERVAL_SECONDS)

if __name__ == "__main__":
    monitor_and_backup()
