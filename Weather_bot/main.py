import requests
from bs4 import BeautifulSoup
from datetime import datetime
import telebot

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

dict_weather = {
    "Ясно": ["Ясно", "Sunny", "преимущественно ясно", 'Clear Night'],
    "Облачно":["Переменная облачность", "облачность", "Облачно"],
    "Дождь":["Дождь", "rain"]
}


def sinoptik_ua():
    r = requests.get(url= "https://sinoptik.ua/погода-кривой-рог", headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find("table", class_="weatherDetails").find("tbody").find_all("tr")
    times = table[0]
    time = []
    for j in times:
        item = j.get_text()
        if item!=" ":
            time.append(item)
    all_weather = table[1]
    weath = []
    for j in all_weather:
        item = j.next_element.next_element
        item = str(item)
        res = item.split('"')
        if len(res)>1:
            weath.append(res[3])
    weath.pop()
    all_info_sinoptik = [time,weath]
    return all_info_sinoptik

def meteopost():
    r = requests.get(url= "https://meteopost.com/city/5695/", headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    table = soup.find("table", class_="weather")
    time = []
    for j in table:
        if len(j)>1:
            inf = j.find_all("td")
            inf = str(inf)
            all_info = (inf.split("<td>")[1])
            all_info = (all_info.split("</td>")[0])
            if (all_info in ["Дата", "ночь", "утро", "день", "вечер"]):
                continue
            time.append(all_info)
            if all_info == "21:00":
                break

    weath = []
    weath_time = []
    for j in table:
        if len(j) > 1:
            inf = j.find_all("td")
            inf = str(inf)
            all_info = (inf.split("<td>")[3])
            all_info = (all_info.split("alt="))
            if len(all_info)<=1:
                continue
            all_info = all_info[1]
            all_info = all_info.split('"')
            all_info = all_info[1]
            weath_time.append(all_info)
    length = len(time)
    for i in range(length):
        weath.append(weath_time[i])
    all_info_meteopost = [time,weath]
    return all_info_meteopost

def weather_com():
    r = requests.get(url= "https://weather.com/ru-RU/weather/hourbyhour/l/Kryvyi+Rih+Dnipropetrovsk+Ukraine?canonicalCityId=87903ec57b2763e8e86a86a5b2cbfa2b8e19b9add21ffa8b5dec42c6a58a1bde", headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    times = soup.find_all("h3", class_="DetailsSummary--daypartName--2FBp2")
    time = []
    for i in times:
        inf = i.get_text()
        time.append(inf)
        if inf == "23:00":
            break
    table = soup.find_all("div", class_="DetailsSummary--condition--24gQw")
    weath = []
    weath_time = []
    for j in table:
        item = j.find("svg").find("title").get_text()
        weath_time.append(item)

    length = len(time)
    for i in range(length):
        weath.append(weath_time[i])
    all_info_meteopost = [time, weath]
    return all_info_meteopost

def message(text):
    # Key bot - 5496869385:AAGjDRX2wSck08zE7RIeBFDrQamILyrg858
    # API бота
    bot = telebot.TeleBot('5496869385:AAGjDRX2wSck08zE7RIeBFDrQamILyrg858')
    bot.config['api_key'] = '5496869385:AAGjDRX2wSck08zE7RIeBFDrQamILyrg858'
    # ID получателя в telegram
    ID = 406690752
    bot.send_message(ID, text)

def check(time,weather1,weather2,weather3):
    for item in weather1[0]:
        item1 = item.split(':')[0]
        if int(time) <= int(item1):
            print(" c - ",item1)

def main():
    sinoptik_list = (sinoptik_ua())
    meteopost_list = (meteopost())
    weather_list = (weather_com())
    time = datetime.now()
    current_time = time.strftime("%H:%M:%S")
    lst_time = str(current_time)
    lst_time = lst_time.split(':')[0]
    print(sinoptik_list)
    print(meteopost_list)
    print(weather_list)
    print(lst_time)
    check(lst_time,sinoptik_list,meteopost_list,weather_list)

if __name__ == "__main__":
    main()