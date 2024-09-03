import requests

def get_random_cat_image():
    '''
    Функция делает запрос к TheCatAPI для получения случайного изображения кошки.
    Возвращает URL изображения, если запрос успешен, иначе возвращает None.
    '''
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
