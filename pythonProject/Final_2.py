def ssh_checkout_negative(ssh_client, cmd, expected_error):
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    if expected_error in out and exit_code != 0:
        return True
    else:
        return False

class Testneg:

    # ... остальной код тестов ...

    def test_nstep1(self, ssh_client, make_bad_arx):
        # test neg 1
        assert ssh_checkout_negative(ssh_client, "cd {}; 7z e {}.{} -o{} -y".format(config["folder_out"], make_bad_arx, config["type"], config["folder_ext"]), "ERROR:"), "test1 FAIL"