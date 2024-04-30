import os
import subprocess
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def get_system_commands():
    path_env = os.getenv('PATH')

    if path_env:
        path_dirs = path_env.split(os.pathsep)
    else:
        return []

    commands = []

    for path_dir in path_dirs:
        try:
            files = os.listdir(path_dir)
            commands.extend([file for file in files if os.access(os.path.join(path_dir, file), os.X_OK)])
        except FileNotFoundError:
            pass

    return commands

def interact_with_shell():
    default_shell = os.getenv('SHELL', 'sh')

    # Open the default system shell
    shell_process = subprocess.Popen(default_shell, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    while True:
        system_commands = get_system_commands()
        completer = WordCompleter(system_commands, ignore_case=True)

        user_input = prompt(os.getcwd() + "/ ", completer=completer)

        if user_input == "?exit":
            shell_process.terminate()
            sys.exit()
        elif user_input == "?help":
            print("Type ?exit to exit the shell.")
        elif user_input.strip() in system_commands:
            subprocess.run(user_input.split())
        elif user_input.startswith("cd "):
            directory = user_input.split(" ", 1)[1]
            try:
                os.chdir(directory)
            except FileNotFoundError:
                print("No such file or directory:", directory)
        elif user_input.startswith("nvim ") or user_input.startswith("vim "):
            editor_command, filename = user_input.split(" ", 1)
            subprocess.run([editor_command, filename])        
        else:
            output = shell_process.communicate(input=user_input.encode())[0].decode()
            print(output.strip())
            interact_with_shell()
interact_with_shell()
