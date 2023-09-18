import subprocess
import string


def test_cli_command(command, text_to_find, word_mode=False):
    try:
        output = subprocess.check_output(command, shell=True, text=True)

        if word_mode:
            translator = str.maketrans('', '', string.punctuation)
            words = output.split()
            words = [word.translate(translator) for word in words]
            text_to_find = text_to_find.translate(translator)

            if text_to_find in words:
                return True
            else:
                return False
        else:
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

if __name__ == "__main__":
    command = "echo 'This is an example sentence!'"
    text_to_find = "example"

    if test_cli_command(command, text_to_find, word_mode=True):
        print(f"Слово '{text_to_find}' найдено в выводе команды '{command}'.")
    else:
        print(f"Слово '{text_to_find}' не найдено в выводе команды '{command}'.")