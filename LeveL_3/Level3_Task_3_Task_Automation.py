import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files_by_type(source_directory):
    """
    Organizes files in the given directory into subfolders based on file extension.
    """
    if not os.path.isdir(source_directory):
        print(f"Error: Directory '{source_directory}' does not exist.")
        return

    file_type_mapping = {
        '.pdf': 'PDFs', '.doc': 'Documents', '.docx': 'Documents',
        '.txt': 'Text_Files', '.xls': 'Spreadsheets', '.xlsx': 'Spreadsheets',
        '.ppt': 'Presentations', '.pptx': 'Presentations',
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images',
        '.gif': 'Images', '.bmp': 'Images', '.svg': 'Images',
        '.mp4': 'Videos', '.mov': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
        '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
        '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
        '.py': 'Python_Scripts', '.js': 'JavaScript_Files',
        '.html': 'Web_Files', '.css': 'Web_Files',
        '.exe': 'Executables', '.dmg': 'Executables',
    }

    for item in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            folder = file_type_mapping.get(ext, 'Others')
            dest_folder = os.path.join(source_directory, folder)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(dest_folder, item))

if __name__ == "__main__":
    # Change this path to the directory you want to organize
    target_dir = r'C:\Users\beast\Downloads'
    os.makedirs(target_dir, exist_ok=True)
    organize_files_by_type(target_dir)
    def select_directory_and_organize():
        root = tk.Tk()
        root.withdraw()
        selected_dir = filedialog.askdirectory(title="Select Directory to Organize")
        if selected_dir:
            organize_files_by_type(selected_dir)

    select_directory_and_organize()