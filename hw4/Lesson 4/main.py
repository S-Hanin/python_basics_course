# -*- coding: utf8 -*-

from website_alive import check_response


def main():
    url = input("Введие url адрес: ")
    if check_response.check_url(url):
        print("Сайт доступен")
    else:
        print("Сайт недоступен")


if __name__ == '__main__':
    main()
