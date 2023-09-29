mport pytest

@pytest.fixture
def login_to_system(site, login_input1_locator, login_input2_locator, login_button_locator):

    input1 = site.find_element("xpath", login_input1_locator)
    input1.send_keys("test")

    input2 = site.find_element("xpath", login_input2_locator)
    input2.send_keys("test")

    btn = site.find_element("css", login_button_locator)
    btn.click()