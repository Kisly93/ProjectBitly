import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse

API_URL = "https://api-ssl.bitly.com"


def create_parse():
    parser = argparse.ArgumentParser(
        description='Введите сайт или сокращенную ссылку'
    )
    parser.add_argument('name')
    return parser


def shorten_link(bitly_token, long_url):
    url = f"{API_URL}/v4/shorten"
    headers = {
        "Authorization": f"Bearer {bitly_token}"
    }
    body = {
        "long_url": long_url
    }
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


def cut_bitlinks(long_url):
    parsed_bitlink = urlparse(long_url)
    cropped_bitlink = f"{parsed_bitlink.netloc}{parsed_bitlink.path}"
    return cropped_bitlink


def count_clicks(bitly_token, long_url):
    url = f"{API_URL}/v4/bitlinks/{cut_bitlinks(long_url)}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {bitly_token}"
    }
    params = {
        "unit": "day",
        "units": "-1"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(bitly_token, long_url):
    url = f"{API_URL}/v4/bitlinks/{cut_bitlinks(long_url)}"
    headers = {
        "Authorization": f"Bearer {bitly_token}"
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    parser = create_parse()
    args = parser.parse_args()
    long_url = args.name
    try:
        if is_bitlink(bitly_token, long_url):
            print("Количество переходов по ссылке битли: ", count_clicks(bitly_token, long_url))
        else:
            print(shorten_link(bitly_token, long_url))
    except requests.exceptions.HTTPError as error:
        print("Вы ввели неправильную ссылку или неверный токен.")


if __name__ == '__main__':
    main()
