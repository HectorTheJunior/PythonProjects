import os
import shutil


def create_folder(path: str, extension: str) -> str:

    """Creating a folder that is named after the file extension passed in"""
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    return folder_path


def sort_files(source_path: str):
    """Sorts files"""
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]

            if extension:
                target_folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)

                shutil.move(file_path, target_path)


def clear_empty_folders(source_path: str):
    """Removes empty folders"""
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for curr_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, curr_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)


def main():
    user_input: str = input("Enter file path you want to sort: \n")

    if os.path.exists(user_input):
        sort_files(user_input)
      """ You don't have to delete that folder. This part can be skipped."""
        clear_empty_folders(user_input)
        print("Files sorted successfully")
    else:
        print("That was invalid path, please provide proper one.")
