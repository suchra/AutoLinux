import yaml
import pytest

from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

def test_step1(
    login_to_system, create_post, error_label_locator, expected_error_message
):

    err_label = site.find_element("xpath", error_label_locator)
    assert err_label.text == expected_error_message