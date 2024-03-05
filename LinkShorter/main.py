import requests
from typing import Final
"""the 'api_key' here is just another file I create to store my Api_Key. I have a problem(bug?!) to set an env variable in Pycharm.."""
from api_key import API
API_KEY: Final[str] = API
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_link(full_link: str):
    params: dict = {'key': API_KEY, 'short': full_link}
    result = requests.get(BASE_URL, params)
    data: dict = result.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print(f'Your link in short version: {short_link}')
        elif url_data['status'] == 1:
            print('The link has already been shortened. Can not be done twice')
        elif url_data['status'] == 2:
            print("Enter valid link.")
        elif url_data['status'] == 3:
            print('The preferred link name is already taken')
        elif url_data['status'] == 4:
            print('Invalid Api Key')
        elif url_data['status'] == 5:
            print('The link has not passed the validation. Includes invalid characters')
        elif url_data['status'] == 6:
            print("The link provided is from a blocked domain")
        elif url_data['status'] == 8:
            print("You have reached your monthly link limit. You can upgrade your subscription plan to add more links.")
        else:
            print(f"Error occurred. Visit: https://cutt.ly/api-documentation/regular-api")


def main():
    user_input: str = input('Enter your link: \n')
    shorten_link(user_input)


main()
