import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
    # test1
    assert checkout("cd /home/zerg/tst; 7z a ../out/arx2", "Everything is Ok"), "test1 FAIL"


def test_step2():
    # test2
    assert checkout("cd /home/zerg/out; 7z e  arx2.7z -o/home/zerg/folder1 -y", "Everything is Ok"), "test2 FAIL"


def test_step3():
    # test3
    assert checkout("cd /home/zerg/out; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_list_files():
    # Test listing files in the archive
    assert checkout("cd /home/zerg/out; 7z l arx2.7z", "Everything is Ok"), "List files test FAIL"


def test_extract_with_paths():
    # Test extracting with preserving paths
    assert checkout("cd /home/zerg/out; 7z x arx2.7z -o/home/zerg/folder2",
                    "Everything is Ok"), "Extract with paths test FAIL"


if __name__ == "__main__":
    test_step1()
    test_step2()
    test_step3()
    test_list_files()
    test_extract_with_paths()