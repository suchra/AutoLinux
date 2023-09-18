import subprocess


def test_cli_command(command, text_to_find):
    try:
        output = subprocess.check_output(command, shell=True, text=True)

        if text_to_find in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    command = "ls /home/user"
    text_to_find = "example_file.txt"

    if test_cli_command(command, text_to_find):
        print(f"Команда '{command}' успешно выполнена и содержит текст '{text_to_find}'.")
    else:
        print(f"Команда '{command}' не выполнена успешно или не содержит текст '{text_to_find}'.")