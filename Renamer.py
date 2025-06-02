import os
import shutil
import tkinter as tk
from tkinter import filedialog

def main():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select multiple files (in order)
    selected_files = filedialog.askopenfilenames(title="Select Files in Order")

    if not selected_files:
        print("No files selected. Exiting.")
        return

    # Create a new folder next to the first selected file
    first_file = selected_files[0]
    folder = os.path.dirname(first_file)
    new_folder = os.path.join(folder, "renamed_files")
    os.makedirs(new_folder, exist_ok=True)

    # Go through each selected file in order and copy/rename it
    for i, filepath in enumerate(selected_files, start=1):
        extension = os.path.splitext(filepath)[1]
        new_name = f"{i}{extension}"
        new_path = os.path.join(new_folder, new_name)

        shutil.copy2(filepath, new_path)

        print(f"Copied: {os.path.basename(filepath)} -> {new_name}")

    print(f"\nDone! Files saved in: {new_folder}")

# Run the program
if __name__ == "__main__":
    main()
