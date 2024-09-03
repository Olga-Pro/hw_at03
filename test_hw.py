import pytest
from main_hw import get_random_cat_image


def test_get_random_cat_image(mocker):
    '''
    Тест, который проверяет успешный запрос и возвращает правильный URL.
    '''
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    cat_image = get_random_cat_image()

    assert cat_image == [{'url': 'https://example.com/cat.jpg'}]


def test_get_random_cat_image_with_error(mocker):
    '''
    Тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.
    '''
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    user_data = get_random_cat_image()
    assert user_data == None