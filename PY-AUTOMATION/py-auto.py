#Python script to automate file management
import os
import shutil


#define the path to the download directory
downloadsfolder= os.path.join(os.path.expanduser('~'), 'Downloads')


#define the target folders for different file types
folders={
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Executables': ['.exe', '.msi'],
    'Scripts': ['.py', '.js', '.sh'],
    'Installers': ['.dmg', '.pkg']
}

#create target folders if they do not exist
for folder in folders.keys():
    target_folder = os.path.join(downloadsfolder, folder)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f'Created folder: {target_folder}')
        
#function to organize files
# Loop through files in the downloads folder
for filename in os.listdir(downloadsfolder):
    file_path = os.path.join(downloadsfolder, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Check file extension and move to the appropriate folder
    for folder, extensions in folders.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            target_folder = os.path.join(downloadsfolder, folder)
            shutil.move(file_path, target_folder)
            print(f'Moved {filename} to {target_folder}')
            break