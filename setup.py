import os
import shutil

os.system("pip install prompt-toolkit")
source = "okralterminal/okterminal.py"
destination = os.path.expanduser("~") 
shutil.move(source, destination)
def add_line_to_shell_file(file_path, line_to_add):
    try:
        file_path = os.path.expanduser(file_path)
        with open(file_path, 'a') as shell_file:
            shell_file.write('\n' + line_to_add + '\n')
        print("Line added successfully to", file_path)
    except Exception as e:
        print("Error:", e)

def choose_shell_file():
    while True:
        choice = input("Which shell file do you want to edit? (Enter 'zsh' for ~/.zshrc or 'bash' for ~/.bashrc): ").lower()
        if choice == 'zsh':
            return "~/.zshrc"
        elif choice == 'bash':
            return "~/.bashrc"
        else:
            print("Invalid choice. Please enter 'zsh' or 'bash'.")

file_path = choose_shell_file()
line_to_add = "python okterminal.py"
add_line_to_shell_file(file_path, line_to_add)

