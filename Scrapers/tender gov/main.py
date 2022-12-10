import os
import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"
}

def parser():
    data = []
    i = 1
    while True:
        r = requests.get(url=f"https://www.tender.gov.mn/en/bidder/list?page={i}&perpage=100&sortField=&sortOrder=&get=1", headers=HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        info = soup.find("table", class_="table sortable").find("tbody").find_all("tr")
        if len(info) <= 1:
            break
        else:
            for element in info:
                href = "https://www.tender.gov.mn" + element.find("a").get("href")
                name = element.find("a").get_text().encode("utf-8")
                direction_of_activity = element.find_all("td")[1].get_text().strip()
                date = element.find_all("td")[2].get_text().strip()
                data.append([name, href, direction_of_activity, date])
        print(f"Parsing {i} page")
        i+=1

    with open("Data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["name of bidder", "url", "direction of activity", "created date"]
        )
    i = 1
    for company in data:
        with open("Data.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                company
            )
        print(f"write in csv file {i} bidder")
        i += 1


parser()
print("finish")