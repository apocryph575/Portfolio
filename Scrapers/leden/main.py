import os
import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.72"
}

url_site = "https://www.thuiswinkel.org/leden/?page="
url_companies = []
data = []


def parser():
    r = requests.get(url=url_site, headers=HEADERS)
    soup = BeautifulSoup(r.text, "lxml")
    number_pages = soup.find('div', id='listingContainer').find("ul", class_="pagination").find_all("a")[-2].get_text()
    print(f"All pages = {number_pages}")
    for page in range(1, int(number_pages) + 1):
        url = f"{url_site}{page}"
        r = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        items = soup.find('div', id='listingContainer').find('div', class_='webshops').find_all('div',
                                                                                                class_='media webshop-list-item shadow rounded py-3 px-4 mb-4')
        for item in items:
            url_comp = item.find("div", class_="media-body").find("a").get("href")
            url_comp = (f"https://www.thuiswinkel.org{url_comp}")
            url_companies.append(url_comp)
        print(f"parsing {page} page")
    for company in url_companies:
        print(company)
        r = requests.get(url=company, headers=HEADERS)
        comp = BeautifulSoup(r.text, "lxml")
        name_company = comp.find('div', class_='bg-white rounded shadow position-relative').find('div',
                                                                                                 class_='p-3 p-md-4').find(
            'div', class_='media').find('div', class_='media-body').find("h1").get_text()
        name_company = name_company[41:]
        name_company = name_company[:-38]
        try:
            url_company = comp.find('div', class_='rounded shadow p-3 p-md-4').find('div', class_='row').find('div',
                                                                                                              class_='col-md-30').find(
                'div', class_='media').find('div', class_='media-body').find("a").get("href")
        except:
            print(f"Url is not on {company}")
            url_company = " "
        try:
            tel_company = comp.find('div', class_='rounded shadow p-3 p-md-4').find('div', class_='row').find('div',
                                                                                                              class_='col-md-30').find_all(
                'div', class_='media')[-2].find("div", class_="media-body").find("a").get_text()
        except:
            print(f"Telephone is not on {company}")
            tel_company = " "
        try:
            KvK_company = comp.find('div', class_='rounded shadow p-3 p-md-4').find('div', class_='row').find('div',
                                                                                                              class_='col-md-30').find_all(
                'div', class_='media')[3].find("div", class_="media-body").get_text()
            KvK_company = KvK_company[50:]
            KvK_company = KvK_company[:-46]
        except:
            print(f"Kvk is not on {company}")
            KvK_company = " "
        data.append([name_company, url_company, tel_company, KvK_company])
        print(f"parsing {company} company")
    print(data)
    with open("Data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["company name", "website url", "phone number", "kvk number"]
        )
    i = 1
    for company in data:
        with open("Data.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                company
            )
        print(f"write in csv file {i} company")
        i += 1


parser()
print("finish")