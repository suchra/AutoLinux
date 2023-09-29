import yaml
import pytest

from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

def test_step1(
    login_input1_locator, login_input2_locator, login_button_locator,
    error_label_locator, expected_error_message
):
    input1 = site.find_element("xpath", login_input1_locator)
    input1.send_keys("test")

    input2 = site.find_element("xpath", login_input2_locator)
    input2.send_keys("test")

    btn = site.find_element("css", login_button_locator)
    btn.click()

    err_label = site.find_element("xpath", error_label_locator)
    assert err_label.text == expected_error_message