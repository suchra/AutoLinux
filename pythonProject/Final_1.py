import yaml
import paramiko
import pytest

# Загрузка конфигурационных данных из файла config.yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)

@pytest.fixture(scope="module")
def ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=config["ip"], username=config["user"], password=config["passwd"])
    yield client
    client.close()


class TestPositive:

    # ... остальной код тестов ...

    def test_step1(self, ssh_client, start_time):
        res = []
        upload_files(ssh_client, config["pkgname"] + ".deb", "/home/{}/{}.deb".format(config["user"], config["pkgname"]))
        res.append(ssh_checkout(ssh_client, "echo '{}' | sudo -S dpkg -i"
                   " /home/{}/{}.deb".format(config["passwd"], config["user"], config["pkgname"]),
                   "Настраивается пакет"))
        res.append(ssh_checkout(ssh_client, "echo '{}' | "
                   "sudo -S dpkg -s {}".format(config["passwd"], config["pkgname"]),
                   "Status: install ok installed"))
        self.save_log(start_time, "log1.txt")
        assert all(res), "test1 FAIL"