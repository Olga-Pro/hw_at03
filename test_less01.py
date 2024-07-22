import pytest
from main_less01 import get_weather


def test_get_weather(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'weather': [{'description': 'clear sky'}],
                                               'main': {'temp': 273.15}
                                               }

    api_key = '01d60d241916f5d850574139c275f457'
    city = 'London'

    weather_data = get_weather(api_key,city)

    assert weather_data == {'weather': [{'description': 'clear sky'}],
                                               'main': {'temp': 273.15}
                                               }


def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    api_key = '01d60d241916f5d850574139c275f457'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == None