import os
import shutil
import glob

# Define source and destination directories
source_dir = "/home/wiola/Downloads"
destination_dir = "/home/wiola/Desktop/OrganizedFiles"

# Define file types and their corresponding folder names
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.txt'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Videos': ['.mp4', '.avi', '.mkv', '.flv', '.mov'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods', '.csv'],
}

# Loop through file types and extensions
for folder, extensions in file_types.items():
    # Create destination folder if it doesn't exist
    folder_path = os.path.join(destination_dir, folder)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Move files with matching extensions from source to destination folder
    for ext in extensions:
        for file in glob.glob(os.path.join(source_dir, f"*{ext}")):
            print(f"Moving {file} to {folder_path}")
            shutil.move(file, folder_path)

