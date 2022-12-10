import speech_recognition
import webbrowser
import os
import keyboard as kb
import subprocess
import time

sr = speech_recognition.Recognizer()

opens = ["открой", "открыть", "запусти", "запустить", "открывай", "play"]
closes = ["закрой", "закрыть"]
programs = {
    "firefox":["мозила", "firefox" , "мозилу", "mozilla", "mozilla firefox"],
    "opera":["opera", "опера", "оперу"],
    "chrome":["google", "гугл", "chrome", "хром"],
    "viber": ["viber", "вайбер"],
    "sublime text": ["sublime", "саблайм", "саблин", "саблайм текст"],
    "telegram": ["telegram"]
    # "Музыка Groove": ["music", "музыка", "плэйлист", "playlist", "музыку"]
}

keyboard = {
    "escape": ["escape"],
    "enter": ["enter", "ввод", "подтвердить"],
    "space":["space", "spaces", "пробел"],
    "tab":["tab", "tabulation", "табуляция", "отступ"],
    "backspace":["backspace", "удалить", "delete"],
    "ctrl+n":["новое", "новая", "new"],
    "ctrl+1": ["первую","1"],
    "ctrl+2": ["вторую", "2"],
    "ctrl+3": ["третью", "3"],
    "ctrl+4": ["четвёртую", "4"],
    "ctrl+5": ["пятую", "5"],
    "ctrl+6": ["шестую", "6"],
    "ctrl+7": ["седьмую", "7"],
    "ctrl+8": ["восьмую", "8"],
    "ctrl+9": ["девятую", "9"],
    "ctrl+w": ["close", "закрой", "закрыть"],
    "ctrl+tab": ["дальше", "следующая", "следующую", "вперёд"],
    "ctrl+shift+tab":["назад", "откат","раньше", "предыдущая", "предыдущую"],
    "win+d": ["свернуть", "скрыть"]
}

write_word = ["напиши", "введи", "набери"]


def program_open(text):
    for item in text:
        for program in programs:
            for i in programs[program]:
                if item == i:
                    name_file = program
                    print(name_file)
                    if name_file == "firefox":
                        firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                        firefox.open('http://www.google.com')
                    elif name_file == "opera":
                        opera = webbrowser.Opera("C:\\Users\\excelent\\AppData\\Local\\Programs\\Opera GX\\launcher.exe")
                        opera.open('http://www.google.com')
                    elif name_file == "chrome":
                        chrome = webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                        chrome.open('http://www.google.com')
                    elif name_file == "viber":
                        subprocess.Popen("C:\\Users\\excelent\\AppData\\Local\\Viber\\Viber.exe")
                    elif name_file == "sublime text":
                        subprocess.Popen("C:\\Program Files\\Sublime Text\\sublime_text.exe")
                    elif name_file == "telegram":
                        subprocess.Popen("C:\\Users\\excelent\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
                    # elif name_file == "Музыка Groove":
                    #     subprocess.Popen("C:\\all_programs_assitant\\Музыка Groove.exe")
                    #     print("open")


def program_close(text):
    for item in text:
        for program in programs:
            for i in programs[program]:
                if item == i:
                    name_file = program
                    os.system(f"taskkill /im {name_file}.exe /f")
                    print(name_file)

def write_keyboard(text):
    print("1")
    for words in text:
        for item in write_word:
            if (item == words):
                ind = text.index(item)+1
                wr_word = text[ind:]
                sentence = " ".join(wr_word)
                print(sentence)
                kb.write(sentence)

def send_keyboard(text):
    for item in text:
        for words in keyboard:
            for word in keyboard[words]:
                if item == word:
                    kb.send(words)
                    print(words)

def say(text):
    print(text)
    for words in text:
        for item in opens:
            if (item == words):
                program_open(text)
                time.sleep(1)
                return
    for words in text:
        for item in closes:
            if (item == words):
               program_close(text)
               time.sleep(1)
               return
    for item in write_word:
        for words in text:
            if (item == words):
                write_keyboard(text)
                time.sleep(1)
                return
    for words in text:
        for item in keyboard:
            for word in keyboard[item]:
                if (word == words):
                    send_keyboard(text)
                    time.sleep(1)
                    return


def main():
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
            if query != " ":
                sentence = query.split()
                say(sentence)
        except Exception as _ex:
            continue

if __name__ == "__main__":
    main()
