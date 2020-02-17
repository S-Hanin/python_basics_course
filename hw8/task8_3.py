# -*- coding: utf8 -*-
"""
Напишите функцию, которая получает два аргумента
  1)путь к файлу изображения jpeg на компьютере (строка);
  2)имя целевого файла (строка)
  отправляет файл HTTP POST запросом на https://postman-echo.com/post .
  В ответе будет получен файл изображения jpeg, в виде octet-stream,
  который нужно раскодировать и сохранить на компьютере под целевым именем,
  переданным в аргументе.
  Функция должна вернуть размер сохраненного файла.
"""
import base64
import pathlib

import requests


def postman_process(img):
    """
    Sends file to https://postman-echo.com/post
    and returns returned files in dict

    :param img: file-like object
    """
    url = "https://postman-echo.com/post"
    response = requests.post(url, files={'file': img})
    return response.json().get("files")


def through_postman_and_back(in_filename: str, out_filename: str):
    """
    Reads file from disk, pass through postman service
    and write it back with given name

    :param in_filename: filepath to read
    :param out_filename: filepath to write
    """
    with open(in_filename, "rb") as rfh, open(out_filename, "wb") as wfh:
        files = postman_process(rfh)
        img_octets = files.get(pathlib.Path(in_filename).name)
        img = base64.b64decode(img_octets.split(",")[-1])
        wfh.write(img)
        return len(img)


if __name__ == '__main__':
    print(f"filesize: {through_postman_and_back('data/img.jpeg', 'data/from_postman.jpeg')} bytes")
