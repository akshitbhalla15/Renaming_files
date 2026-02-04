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
