import os
import shutil

# Folder to organize (change if needed)
SOURCE_FOLDER = os.path.expanduser("~/Downloads")

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    for file_name in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        for folder, extensions in FILE_TYPES.items():
            if file_name.lower().endswith(tuple(extensions)):
                destination = os.path.join(SOURCE_FOLDER, folder)
                os.makedirs(destination, exist_ok=True)
                shutil.move(file_path, destination)
                break
        else:
            others = os.path.join(SOURCE_FOLDER, "Others")
            os.makedirs(others, exist_ok=True)
            shutil.move(file_path, others)

if __name__ == "__main__":
    organize_files()
    print("Files organized successfully!")