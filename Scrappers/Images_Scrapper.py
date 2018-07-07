from bs4 import BeautifulSoup   # Для навигации по HTML
import requests                 # Для отправки запросов на сайты
from io import BytesIO          # Input output
from PIL import Image           # Работа с картинками
import os                       # Для проверки директорий и файлов

def StartSearch():
    search = input("Search for: ")
    My_Params = {"q": search}
    dir_name = search.replace(" ", "_").lower() # формируем имя директории куда будем сохранять картинки

    if not os.path.isdir(dir_name): # Create dir if not exist
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=My_Params)

    My_Soup = BeautifulSoup(r.text,"html.parser")

    links = My_Soup.findAll("a", {"class": "thumb"})

    for item in links:
        # в ходе отладки всплывали ошибки. Используем try дабы отловить их.
        try:
            img_obj = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1] # формируем название картинки
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except OSError:
                print("Invalid name of image")
            except:
                print("Could not save image")
        except:
            print("Could not connect")

    StartSearch()

StartSearch()