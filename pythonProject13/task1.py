import requests
import json
import pytest

base_url = "https://test-stand.gb.ru/api/posts"

def create_post(title, description, content):
    data = {
        "title": title,
        "description": description,
        "content": content
    }
    response = requests.post(base_url, json=data)
    return response

def check_post_by_description(description):
    response = requests.get(base_url)
    posts = response.json()
    for post in posts:
        if post["description"] == description:
            return True
    return False

@pytest.mark.parametrize("title, description, content", [("Заголовок", "Описание", "Содержание")])
def test_create_post_and_check_by_description(title, description, content):
    response = create_post(title, description, content)

    assert response.status_code == 201

    assert check_post_by_description(description) == True

if __name__ == "__main__":
    pytest.main([__file__])

