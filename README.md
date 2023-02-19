# Обрезка ссылок с помощью Bitly

Проект создан для удобного сокращения длинных ссылок с помощью сервиса bitly.com.

Также проект позволяет получать количество переходов по уже созданным bitly-ссылкам.

## Как установить
Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

``` python
pip install -r requirements.txt
```

Получите персональный токен на сайте [bitly.com](https://dev.bitly.com/docs/getting-started/authentication/) и сохраните его в файле .env в корневой директории проекта:

```
BITLY_TOKEN=<ваш токен>
```
### Запустите скрипт:

```
python main.py <ваша ссылка>
```
В качестве аргумента скрипт принимает длинную ссылку или сокращенную bitly-ссылку.

Если передана длинная ссылка, скрипт создаст bitly-ссылку и выведет ее в консоль.

Если передана сокращенная bitly-ссылка, скрипт выведет количество переходов по ней в консоль.

## Пример использования:

```
$ python main.py https://dvmn.org/
https://bit.ly/3Y0CSmU
```
```
python main.py https://bit.ly/3Y0CSmU
Количество переходов по ссылке битли:  1
```
## Цели проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmns.org](https://dvmn.org/). Обучение работы с API, работа с библиотекой requests, разбор параметров командной строки с помощью argparse.

# Cropping links with Bitly
The project was created to conveniently shorten long links using the bitly.com service.

The project also allows you to get the number of clicks on already created bitly links.

## How to install
Python3 should already be installed. Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:

```
pip install -r requirements.txt
```
Get a personal token from [bitly.com](https://dev.bitly.com/docs/getting-started/authentication/) and save it in an .env file in the project root directory:

```
BITLY_TOKEN=<your token>
```
## Run the script:
```
python main.py <your link>
```
The script accepts a long link or a shortened bitly link as an argument.

If a long link is entered, the script will create a bitly link and print it to the console.

If a shortened bitly link is entered, the script will print the number of clicks on it to the console.

## Usage example:
```
python main.py https://dvmn.org/
https://bit.ly/3Y0CSmU
```
```
python main.py https://bit.ly/3Y0CSmU
Number of clicks on the bitley link: 1
```
## Project Goals
The code was written for educational purposes on the [dvmns.org](https://dvmn.org/) online course for web developers. Learning how to work with the API, working with the requests library, parsing command line parameters using argparse.