File Handling Programs in Python
This repository contains two simple Python programs demonstrating file handling operations such as reading, writing, appending, and handling errors using exceptions.

🧩 Program 1: File Reading with Exception Handling
File: sample.txt
Description:
This program attempts to read and display the content of a file named sample.txt.
If the file does not exist, it gracefully handles the error using a try-except block.

Code Overview:
Opens sample.txt in read mode ("r").
Reads and prints the file’s content.
Catches FileNotFoundError if the file doesn’t exist and displays an error message.

Code Overview:
Takes input from the user and writes it to output.txt (creates a new file or overwrites existing content).
Takes another input and appends it to the same file.
Reads the final file content and displays it in the console.

⚙️ How to Run
Save both code blocks in a .py file (e.g., file_handling.py).
Make sure Python is installed on your system.
Run the script using:
python file_handling.py

🧠 Concepts Used
File handling modes ("r", "w", "a")
Exception handling (try-except)
Reading and writing text files
Working with user input
