import os
import shutil

def organize_files(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("❌ The folder you entered does not exist.")
        return

    # Get all items inside the folder
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        # Only organize files (skip folders)
        if os.path.isfile(item_path):
            # Get file extension (ex: "jpg", "png", "txt")
            extension = item.split(".")[-1].lower()

            # Create a folder name like "jpg_files"
            folder_name = extension + "_files"
            folder_full_path = os.path.join(folder_path, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_full_path):
                os.mkdir(folder_full_path)

            # Move the file into the new folder
            shutil.move(item_path, os.path.join(folder_full_path, item))

    print("✔ All files have been organized successfully!")


def main():
    print("===== SIMPLE FILE ORGANIZER =====")
    folder_path = input("Enter the folder path: ").strip()
    organize_files(folder_path)


if __name__ == "__main__":
    main()

