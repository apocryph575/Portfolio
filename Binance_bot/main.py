import requests
import json
import telebot

bot_info = []
# API бота

def get_api_tele():
    with open("telebot_api.txt", "r") as telfile:
        for stringfile in telfile:
            first_bot = stringfile.split()
            bot_info.append(" ".join(first_bot))
    api_key = str(bot_info[0].split("=")[1])
    id_key = bot_info[1].split("=")[1]
    bot = telebot.TeleBot(api_key[1:])
    bot.config['api_key'] = api_key[1:]
    identif = id_key[1:]
    return identif, bot


def message(bot, id_key, text):
    bot.send_message(id_key, text)

def get_info(name_crypto):
    base = "https://fapi.binance.com"
    path = "/fapi/v1/ticker/price"
    url = base+path
    param = {'symbol': name_crypto}
    r = requests.get(url, params=param)
    return r.json()

def read_info_json():
    with open("info.json", "r") as file:
        data = json.load(file)
    return data

def main():
    id_k, bot_k = get_api_tele()

    data_info = read_info_json()
    i = 0
    while True:
        for item in data_info["prices"]:
            correct_name = item["symbol"]
            try:
                info = get_info(correct_name)
                correct_price = info["price"]
                if float(correct_price) < float(item["buy"]):
                    message(bot_k, id_k, f"Time to BUY - {correct_name}, correct price = {correct_price}")
                elif float(correct_price) > float(item["sell"]):
                    message(bot_k, id_k, f"Time to SELL - {correct_name}, correct price = {correct_price}")
                else:
                    continue
            except:
                continue
        i += 1



if __name__ == "__main__":
    main()




