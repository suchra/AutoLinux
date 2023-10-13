import subprocess
import pytest
import time

# Модуль для взаимодействия с объектами страниц
class ArchivePage:
    def __init__(self, archive_type):
        self.archive_type = archive_type

    def create_archive(self):
        cmd = f"cd /home/zerg/tst; 7z a ../out/arx2 -t{self.archive_type}"
        return self._execute_command(cmd)

    def extract_archive(self):
        cmd = f"cd /home/zerg/out; 7z e arx2.7z -o/home/zerg/folder1 -y -t{self.archive_type}"
        return self._execute_command(cmd)

    def test_archive(self):
        cmd = f"cd /home/zerg/out; 7z t arx2.7z -t{self.archive_type}"
        return self._execute_command(cmd)

    def list_files(self):
        cmd = f"cd /home/zerg/out; 7z l arx2.7z -t{self.archive_type}"
        return self._execute_command(cmd)

    def extract_with_paths(self):
        cmd = f"cd /home/zerg/out; 7z x arx2.7z -o/home/zerg/folder2 -t{self.archive_type}"
        return self._execute_command(cmd)

    def _execute_command(self, cmd):
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        return "Everything is Ok" in result.stdout and result.returncode == 0

# Фикстура для записи статистики в файл после каждого шага теста
@pytest.fixture(autouse=True)
def record_statistics():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # Ваш код для получения статистики
    with open("/путь/к/файлу/stat.txt", "a") as f:
        f.write(f"{current_time}, количество файлов, размер файла, статистика загрузки процессора\n")

# Тесты, использующие объект страницы
def test_archive_operations():
    archive_page = ArchivePage(archive_type="zip")

    assert archive_page.create_archive(), "Create archive test FAIL"
    assert archive_page.extract_archive(), "Extract archive test FAIL"
    assert archive_page.test_archive(), "Test archive test FAIL"
    assert archive_page.list_files(), "List files test FAIL"
    assert archive_page.extract_with_paths(), "Extract with paths test FAIL"

if __name__ == "__main__":
    pytest.main()