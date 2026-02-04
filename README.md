# Sequential File Renamer

A simple, lightweight Python script to batch-rename files numerically based on user selection.

## ✨ Features
- **User-Friendly:** Opens a native file picker dialog via Tkinter.
- **Safe:** Creates a separate folder (`renamed_files`) to prevent accidental data loss; it copies rather than moves.
- **Ordered:** Renames files (1, 2, 3...) based on the selection order.
- **Extension Aware:** Automatically detects and preserves the original file extension (e.g., `.png`, `.txt`, `.docx`).

## 🚀 How to Use

### Prerequisites
- **Python 3.x**
- **Tkinter** (Standard with most Python installations. On Linux, you may need `sudo apt-get install python3-tk`).

### Installation
1. Clone this repository or download `rename_script.py`.
2. Ensure you have Python installed.

### Running the Script
1. Run the script via terminal or command prompt:
   ```bash
   python rename_script.py
   A file dialog window will appear. Select the files you want to rename.
   
2. A file dialog window will appear. **Select the files** you want to rename.

> **Note:** The order in which files are selected (or the order your OS passes them) determines their new number.

3. The script will process the files and print the status to the console.

### Output

A new folder named `renamed_files` is created in the same directory as the source files.

* Original: `photo_vacation.jpg`
* New: `renamed_files/1.jpg`

Note: The order in which files are selected (or the order your OS passes them) determines their new number.

The script will process the files and print the status to the console.

Output

A new folder named renamed_files is created in the same directory as the source files.

Original: photo_vacation.jpg

New: renamed_files/1.jpg

📂 Project Structure
.
├── rename_script.py    # Main executable script
└── renamed_files/      # (Generated) Destination for renamed files

📝 License
MIT License - Feel free to use and modify for your own projects!
