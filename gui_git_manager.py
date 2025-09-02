#! /usr/bin/env python3

import os
import subprocess
import tkinter as tk
from tkinter import simpledialog, scrolledtext

def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout + result.stderr

def initialize_git_repo():
    output = subprocess.run(["git", "init"], capture_output=True, text=True)
    return output.stdout if output.returncode == 0 else output.stderr

def check_status():
    output = run_command(['git', 'status'])
    output_text.insert(tk.END, output + "\n")

import os
from tkinter import simpledialog

def stage_changes():
    files = simpledialog.askstring(
        "Input",
        "Enter the files to stage (separated by space):"
    )
    if files:
        file_list = [file.strip() for file in files.split() if file.strip()]  # Trim whitespace and filter empty strings
        invalid_files = [file for file in file_list if not os.path.isfile(file)]  # Check for invalid files

        if invalid_files:
            output_text.insert(tk.END, f"Invalid files: {', '.join(invalid_files)}\n")
            return

        output = run_command(['git', 'add'] + file_list)
        output_text.insert(tk.END, output + "\n")


def commit_changes():
    message = simpledialog.askstring("Input", "Enter commit message:")
    if message:
        output = run_command(['git', 'commit', '-m', message])
        output_text.insert(tk.END, output + "\n")

def push_changes():
    branch = simpledialog.askstring(
        "Input",
        "Enter branch name (default is 'main'):",
        initialvalue='main'
    )
    output = run_command(['git', 'push', 'origin', branch])
    output_text.insert(tk.END, output + "\n")

def initialize_git_repo():
    output = run_command(['git', 'init'])
    output_text.insert(tk.END, output + "\n")
    output = run_command(['git', 'add .'])
    output_text.insert(tk.END, output + "\n")
    output = run_command(['git', 'commit', '-m', "Initial commit"])
    output_text.insert(tk.END, output + "\n")


def main():
    global output_text
    # Get the current directory
    current_directory = os.getcwd()
    os.chdir(current_directory)
    # Initialize the Git repository if it doesn't exist and capture output
    if not os.path.isdir(os.path.join(current_directory, '.git')):
        init_output = initialize_git_repo()
        output_text.insert(tk.END, init_output + "\n")  # Display output of init

    # Create the main window
    root = tk.Tk()
    root.title("Git Manager")
    root.configure(bg='#2E2E2E')  # Set the background color of the main window
    # common button settings
    button_properties = {
        'bg': '#2E2E2E',
        'fg': 'lightgray',
        'width': 20  # fixed width for all buttons
    }

    btn_check_status = tk.Button(
        root,
        text="Check Status",
        command=check_status,
        **button_properties
    )
    btn_check_status.pack(pady=5)

    btn_stage_changes = tk.Button(
        root,
        text="Stage Changes",
        command=stage_changes,
        **button_properties
    )
    btn_stage_changes.pack(pady=5)

    btn_commit_changes = tk.Button(
        root,
        text="Commit Changes",
        command=commit_changes,
        **button_properties
    )
    btn_commit_changes.pack(pady=5)

    btn_push_changes = tk.Button(
        root,
        text="Push Changes",
        command=push_changes,
        **button_properties
    )
    btn_push_changes.pack(pady=5)

    # Text area for output of commands
    output_text = scrolledtext.ScrolledText(
        root,
        width=80,
        height=15,
        bg='#2E2E2E',        # Set background color to black
        fg='lightgray'     # Set text color to light gray
    )
    output_text.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
